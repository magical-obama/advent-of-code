f = open("input.txt", "r")

strValues = f.read().split("\n")

intValues = []

for i in strValues:
    intValues.append(int(i))

for x in intValues:
    for y in intValues:
        for z in intValues:
            if x + y + z == 2020:
                print(str(x) + " " + str(y) + " " + str(z))

# Link: https://adventofcode.com/2020/day/1#part2
# Antwort: 286977330