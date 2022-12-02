def get_rules(rules):
    rules_dict = {}
    num_direct_contain = 0
    num_contain = 0
    for i in range(len(rules)):
        container_bag = rules[i][1][0] + " " + rules[i][1][1]
        if rules[i][-1] == True:
            inside_bags = [rules[i][1][5] + " " + rules[i][1][6], rules[i][1][9] + " " + rules[i][1][10]]
        # elif rules[i][-1] == False:
        #     inside_bags = [rules[i][1][5] + " " + rules[i][1][6]]
        else:
            inside_bags = [rules[i][1][5] + " " + rules[i][1][6]]
        rules_dict[container_bag] = inside_bags
    for i in rules_dict:
        if rules_dict[i].count("shiny gold") == 1:
            num_direct_contain += 1
            if rules_dict[i].count(True) == 0:
                rules_dict[i].append(True)
        for i in rules_dict:
            if rules_dict[i].count(True) >= 1:
                rules_dict[i][-1] = False
                num_contain += 1

    print(rules_dict)
    print(num_direct_contain, num_contain)

f = open("input.txt", "r")
rules = f.read().split("\n")


for i in range(len(rules)):
    rules[i] = [rules[i], rules[i].split()]
    rules[i][1][-1] = rules[i][1][-1][:-1]
    for x in range(len(rules[i][1])):
        if rules[i][1][x].count(",") == 1:
            rules[i][1][x] = rules[i][1][x][:-1]
            if True not in rules[i]:
                rules[i].append(True)
    if True not in rules[i]:
        rules[i].append(False)


# print(rules_)
get_rules(rules)