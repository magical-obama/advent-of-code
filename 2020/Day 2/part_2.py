f = open("input.txt", "r")
values = f.read().split("\n")
lines = []
boolValid = False
numValid = 0

for i in values:
    lines.append(i.split(":"))

for x in range(len(lines)):
    boolValid = False
    lines[x][1] = lines[x][1].strip()
    lines[x].insert(2, lines[x][0][:-2])
    lines[x].insert(3, lines[x][2].split("-"))
    lines[x].append(lines[x][0][-1])
    pos1 = int(lines[x][3][0]) - 1
    # print(pos1)
    pos2 = int(lines[x][3][1]) - 1
    char = lines[x][4]
    # print(char)
    # if lines[x][1][pos1] == char and lines[x][1][pos2] == char:
    #     break
    # print(lines[x][1][pos1])
    if lines[x][1][pos1] == char:
        boolValid = True
    if lines[x][1][pos2] == char:
        boolValid = not boolValid
    if boolValid == True:
        numValid += 1

# print(lines)
print(f"{numValid} are Valid")

# Link: https://adventofcode.com/2020/day/2#part2
# Antwort: 747