import numpy as np

input_data = ""
with open("input") as f:
    input_data = f.read()

elves_items = input_data.split('\n\n')

# print(elves_items)

elves = []

for i in range(len(elves_items)):
    elf_backpack = elves_items[i].splitlines()
    for item in range(len(elf_backpack)):
        elf_backpack[item] = int(elf_backpack[item])
    elves.append(elf_backpack)
# print(elves)

elf_sum = list(map(lambda x: sum(x), elves))

del elves, elves_items, elf_backpack, input_data, item, f, i

print(max(elf_sum))
