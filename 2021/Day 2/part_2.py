file_str = open("input.txt").read()
input_list = file_str.splitlines()

pos = [0, 0, 0] # Index 0: horizontal Pos, Index 1: depth, Index 2: Aim
com_list = []

legend = {
    "down": 1,
    "up": -1,
    "forward": 1
}

for element in input_list:
    com_list.append((element.split(' ')[0], element.split(' ')[1]))

for com in com_list:
    if com[0] == "down" or com[0] == "up":
        pos[2] += legend[com[0]] * int(com[1])
    else:
        pos[0] += legend[com[0]] * int(com[1])
        pos[1] += legend[com[0]] * int(com[1]) * pos[2]

print(pos)
print(pos[0] * pos[1])