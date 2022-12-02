import re

f = open("input.txt", "r")
passports = f.read().split("\n\n")
numValid = 0
requiredFields = 0

required = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
]

for i in range(len(passports)):
    passports[i] = passports[i].replace(" ", "\n")
    passports[i] = passports[i].split("\n")

    for x in range(len(passports[i])):
        passports[i][x] = passports[i][x].split(":")
        for y in required:
            if passports[i][x][0] == y:
                if required.index(y) == 0:
                    if 1920 <= int(passports[i][x][1]) <= 2002:
                        requiredFields += 1
                        break
                elif required.index(y) == 1:
                    if 2010 <= int(passports[i][x][1]) <= 2020:
                        requiredFields += 1
                        break
                elif required.index(y) == 2:
                    if 2020 <= int(passports[i][x][1]) <= 2030:
                        requiredFields += 1
                        break
                elif required.index(y) == 3:
                    if passports[i][x][1][-2:] == "cm":
                        if 150 <= passports[i][x][1][:-2] <= 193:
                            requiredFields += 1
                            break
                    elif passports[i][x][1][-2:] == "in":
                        if 59 <= passports[i][x][:-2] <= 76:
                            requiredFields += 1
                            break
                elif required.index(y) == 4:
                    if re.search("#[0-9a-f]{6}", passports[i][x][1][:-2]) != None:
                        requiredFields += 1
                        break
                elif required.index(y) == 5:
                    if 2010 <= int(passports[i][x][1]) <= 2020:
                        requiredFields += 1
                        break
                elif required.index(y) == 6:
                    if 2010 <= int(passports[i][x][1]) <= 2020:
                        requiredFields += 1
                        break
                
    if requiredFields >= len(required):
        numValid += 1
    requiredFields = 0


print(numValid)

# Link: https://adventofcode.com/2020/day/4#part2
# Antwort: ?