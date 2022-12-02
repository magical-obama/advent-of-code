file_str = open("input.txt").read()
input_list = file_str.splitlines()

pos = [0, 0] # Index 0: horizontal, Index 1: depth

input_dict = []

legend = {
    "forward": 1,
    "down": 1,
    "up": -1
}

for element in input_list:
    input_dict.append((element.split(' ')[0], element.split(' ')[1]))

print(input_dict)

for element in input_dict:
    if element[0] == "down" or element[0] == "up":
        pos[1] += legend[element[0]] * int(element[1])
    else:
        pos[0] += legend[element[0]] * int(element[1])

print(pos)
print(pos[0] * pos[1])
