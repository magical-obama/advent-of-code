def is_element_next_to_previous(pos_element: tuple[int, int], pos_previous: tuple[int, int]):
    if pos_element == pos_previous:
        return True
    elif pos_element[0] in range(pos_previous[0] - 1, (pos_previous[0] + 1) + 1) and pos_element[1] in range(pos_previous[1] - 1, (pos_previous[1] + 1) + 1):
        return True
    return False


def move_element(index: int):
    assert len(snake) > index > 0
    element = snake[index]
    prev_element = snake[index - 1]
    if prev_element[0] == element[0]:
        if prev_element[1] > element[1]:
            element[1] += 1
        elif prev_element[1] < element[1]:
            element[1] -= 1
    elif prev_element[1] == element[1]:
        if prev_element[0] > element[0]:
            element[0] += 1
        elif prev_element[0] < element[0]:
            element[0] -= 1
    elif prev_element[0] != element[0] and prev_element[1] != element[1]:
        horiz_dir = 1 if prev_element[0] > element[0] else -1
        vert_dir = 1 if prev_element[1] > element[1] else -1
        element[0] += horiz_dir
        element[1] += vert_dir
    snake[index] = element


def move_snake(command: tuple[str, int]):
    global snake
    for index in range(len(snake)):
        if index == 0:
            move_head(command)
        else:
            move_element(index)

    tail_visited_pos.add(tuple(snake[-1]))


def move_head(command: tuple[str, int]):
    global snake
    head_pos = snake[0]
    for iteration in range(command[1]):
        if command[0] == 'R':
            head_pos[0] += 1
        elif command[0] == 'D':
            head_pos[1] += 1
        elif command[0] == 'L':
            head_pos[0] -= 1
        elif command[0] == 'U':
            head_pos[1] -= 1
        snake[0] = head_pos


with open('input') as f:
    input_file = f.read()

input_data = [(line.split()[0], int(line.split()[1])) for line in input_file.splitlines()]

# print(input_data)

tail_visited_pos: set[tuple[int, int]] = set()
tail_visited_pos.add((0, 0))

snake = [[0, 0] for _ in range(10)]

for movement in input_data:
    move_snake(movement)

# print(tail_visited_pos)
print("Solution:", len(tail_visited_pos))
