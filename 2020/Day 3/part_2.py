def check_trees(x_step, y_step):
    trees = 0
    x = 0
    y = 0
    while y < area[0]:
        if lines[y][x] == "#":
            trees += 1
        x += x_step
        y += y_step
    return trees

f = open("input.txt", "r")
lines = f.read().split("\n")
f.close()

for i in range(len(lines)):
    pattern = 100 * lines[i]
    lines[i] = pattern

area = [len(lines), len(lines[0])] # Warning! [y, x]

totalTrees = check_trees(1, 1) * check_trees(3, 1) * check_trees(5, 1) * check_trees(7, 1) * check_trees(1, 2)

print(f"{totalTrees} Trees")

# Link: https://adventofcode.com/2020/day/3#part2
# Antwort: 3952146825