f = open("input.txt", "r")
lines = f.read().split("\n")
f.close()

trees = 0
x = 0
y = 0

for i in range(len(lines)):
    pattern = 50 * lines[i]
    lines[i] = pattern

area = [len(lines[0]), len(lines)] # Warning! [y, x]

while y < area[1]:
    if lines[y][x] == "#":
        trees += 1
    x += 3
    y += 1

print(f"I will hit {trees} trees")

# Link: https://adventofcode.com/2020/day/3
# Antwort: 205