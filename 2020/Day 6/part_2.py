import string

def get_group_yes(group_ans):
    group_yes = []
    num_all_yes = 0
    people = len(group_ans)
    if people == 1:
        return len(group_ans[0])
    for i in range(people):
        for x in range(len(group_ans[i])):
            group_yes.append(group_ans[i][x])
    for i in string.ascii_lowercase:
        if group_yes.count(i) >= people:
            num_all_yes += 1
                
    return num_all_yes

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

print("No of all yesses:", get_all_yes())

# Link: https://adventofcode.com/2020/day/6#part2
# Antwort: 3290