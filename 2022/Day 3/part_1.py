import string

with open('input') as f:
    input_data = f.read()

backpacks = input_data.splitlines()

print(backpacks)
print(len(backpacks))

item_index = []

for backpack in backpacks:
    items_in_backpack = []
    for item in backpack:
        if item not in items_in_backpack:
            items_in_backpack.append(item)
    item_index.append(items_in_backpack)

for i in range(len(backpacks)):
    backpack = backpacks[i]
    num_items_per_compartment = len(backpack) // 2
    backpacks[i] = [backpack[:num_items_per_compartment], backpack[num_items_per_compartment:]]

print(backpacks)
print(item_index)

duplicate_items = []

for i in range(len(backpacks)):
    backpack = backpacks[i]
    possible_items = item_index[i]

    for item in possible_items:
        if item in backpack[0] and item in backpack[1]:
            duplicate_items.append(item)

print(duplicate_items)
print(len(duplicate_items))

letter_values = list(enumerate(string.ascii_letters, 1))
letter_dict = {}
for i in range(len(letter_values)):
    letter_value, letter = letter_values[i]
    letter_dict[letter] = letter_value

print(letter_dict)

backpack_values = [letter_dict[i] for i in duplicate_items]

print(backpack_values)
print('Solution:', sum(backpack_values))
