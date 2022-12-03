import string

with open('input') as f:
    input_data = f.read()

backpacks = input_data.splitlines()

print(backpacks)
print(len(backpacks))

groups = []
for index in range(len(backpacks)):
    if index % 3 == 0:
        groups.append(backpacks[index:index + 3])

print(groups)
print(len(groups))

group_badges = []
for group in groups:
    for letter in string.ascii_letters:
        if letter in group[0] and letter in group[1] and letter in group[2]:
            group_badges.append(letter)

print(group_badges)

letter_values = list(enumerate(string.ascii_letters, 1))
letter_dict = {}
for i in range(len(letter_values)):
    letter_value, letter = letter_values[i]
    letter_dict[letter] = letter_value

print(letter_dict)

group_badges_values = [letter_dict[i] for i in group_badges]

print(group_badges_values)
print('Solution:', sum(group_badges_values))
