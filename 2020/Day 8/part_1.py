f = open("input.txt", "r")
lines = f.read().split("\n")

num = 0

for i in range(len(lines)):
    lines[i] = [lines[i], lines[i].split()]

i = 0
done = []
while i < len(lines):
    if done.count(i) >= 1:
        print(i)
        break
    done.append(i)
    if lines[i][1][0] == "acc":
        if lines[i][1][1][0] == "+":
            num += int(lines[i][1][1][1:])
        # elif lines[i][1][1][0] == "-":
        #     num -= int(lines[i][1][1][1:])
        else:
            num -= int(lines[i][1][1][1:])
    if lines[i][1][0] == "jmp":
        if lines[i][1][1][0] == "+":
            i += int(lines[i][1][1][1:])
        else:
            i -= int(lines[i][1][1][1:])
        # elif lines[i][1][1][0] == "-":
        #     i -= int(lines[i][1][1][1:])
        continue

    i += 1

print(done)
print("Accumulator:", num)

# Link: https://adventofcode.com/2020/day/8
# Antwort: 1548