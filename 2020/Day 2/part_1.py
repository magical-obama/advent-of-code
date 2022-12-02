f = open("input.txt", "r")
values = f.read().split("\n")

lines = []
numValid = 0

for i in values:
    lines.append(i.split(":"))

for x in range(len(lines)):
    lines[x][1] = lines[x][1].strip()
    lines[x].insert(2, lines[x][0][:-2])
    lines[x].insert(3, lines[x][2].split("-"))
    lines[x].append(lines[x][0][-1])

    min = int(lines[x][3][0])
    max = int(lines[x][3][1])

    if lines[x][1].count(lines[x][4]) >= min and lines[x][1].count(lines[x][4]) <= max:
        numValid += 1

# print(lines)
print(f"{numValid} are Valid")

# Link: https://adventofcode.com/2020/day/2
# Antwort: 424