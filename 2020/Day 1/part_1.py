f = open("input.txt", "r")

strValues = f.read().split("\n")

intValues = []

for i in strValues:
    intValues.append(int(i))

for x in intValues:
    for y in intValues:
        if x + y == 2020:
            print(str(x) + " " + str(y))

# Link: https://adventofcode.com/2020/day/1
# Antwort: 1020036