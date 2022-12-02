def get_group_yes(group_ans):
    group_yes = []
    people = len(group_ans)
    for i in range(people):
        for x in range(len(group_ans[i])):
            if group_ans[i][x] not in group_yes:
                group_yes.append(group_ans[i][x])
    return len(group_yes)

def get_all_yes():
    all_yes = 0
    for i in range(len(groups)):
        all_yes += get_group_yes(groups[i][1])
    return all_yes

# Functions End

f = open("input.txt", "r")
groups = f.read().split("\n\n")

for i in range(len(groups)):
    groups[i] = [groups[i], groups[i].split("\n")]

print("No of yesses:", get_all_yes())

# Link: https://adventofcode.com/2020/day/6
# Antwort: 6583