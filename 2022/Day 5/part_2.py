import re
import string

operation_regex = 'move ([0-9]+) from ([0-9]+) to ([0-9]+)'

with open('input') as f:
    input_data = f.read()

raw_stacks, raw_operations = input_data.split('\n\n')

print(raw_stacks)
stacks = [[] for i in range(9)]

splitted_stacks = raw_stacks.splitlines()
splitted_stacks.reverse()

for line in splitted_stacks:
    for stack in range(9):
        line_index = 1 + stack * 4
        if line[line_index] != ' ' and not line[line_index] in string.digits:
            stacks[stack].append(line[line_index])

print(stacks)

raw_operations = raw_operations.splitlines()
operations = []
for operation in raw_operations:
    operations.append(re.findall(operation_regex, operation))

for i in range(len(operations)):
    operation = operations[i]
    operations[i] = [int(i) for i in operation[0]]

for operation in operations:
    num = operation[0]
    from_stack_index = operation[1] - 1
    to_stack_index = operation[2] - 1
    to_move = stacks[from_stack_index][-num:]
    stacks[from_stack_index] = stacks[from_stack_index][:-num]
    stacks[to_stack_index].extend(to_move)


print(operations)
print(stacks)
top_crates = [stack[-1] for stack in stacks]

print('Solution:', ''.join(top_crates))
