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
                requiredFields += 1
    if requiredFields >= len(required):
        numValid += 1
    requiredFields = 0


print(numValid)

# Link: https://adventofcode.com/2020/day/4
# Antwort: 190