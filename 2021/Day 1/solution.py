increasing_count = 0 
previous_sum = 0
previous_numbers = []
f = open("input.txt")
file_list = f.read().split('\n')
numbers = []
for item in file_list:
    numbers.append(int(item))


for number in numbers: 
    sum = 0 
    if len(previous_numbers) == 3: 
        number_to_remove = previous_numbers[0]
        previous_numbers.remove(number_to_remove)

    previous_numbers.append(number)

    if len(previous_numbers) > 2:
        for previous_number in previous_numbers:
            sum += previous_number

    if sum > previous_sum and previous_sum != 0:
        increasing_count += 1

    previous_sum = sum

print(f"Part 2: {increasing_count}")