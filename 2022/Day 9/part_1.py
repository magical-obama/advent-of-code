def is_tail_next_to_head():
    global head_pos, tail_pos
    if head_pos == tail_pos:
        return True
    elif tail_pos[0] in range(head_pos[0] - 1, (head_pos[0] + 1) + 1) and tail_pos[1] in range(head_pos[1] - 1, (head_pos[1] + 1) + 1):
        return True
    return False


def move_tail():
    global head_pos, tail_pos, tail_visited_pos
    if head_pos[0] == tail_pos[0]:
        if head_pos[1] > tail_pos[1]:
            tail_pos[1] += 1
        elif head_pos[1] < tail_pos[1]:
            tail_pos[1] -= 1
    elif head_pos[1] == tail_pos[1]:
        if head_pos[0] > tail_pos[0]:
            tail_pos[0] += 1
        elif head_pos[0] < tail_pos[0]:
            tail_pos[0] -= 1
    elif head_pos[0] != tail_pos[0] and head_pos[1] != tail_pos[1]:
        horiz_dir = 1 if head_pos[0] > tail_pos[0] else -1
        vert_dir = 1 if head_pos[1] > tail_pos[1] else -1
        tail_pos[0] += horiz_dir
        tail_pos[1] += vert_dir
    tail_visited_pos.add(tuple(tail_pos))


def move_head(command: tuple[str, int]):
    global head_pos, tail_pos
    for iteration in range(command[1]):
        if command[0] == 'R':
            head_pos[0] += 1
        elif command[0] == 'D':
            head_pos[1] += 1
        elif command[0] == 'L':
            head_pos[0] -= 1
        elif command[0] == 'U':
            head_pos[1] -= 1
        tail_movement_counter = 0
        while not is_tail_next_to_head():
            move_tail()
            tail_movement_counter += 1
        assert tail_movement_counter <= 1


with open('input') as f:
    input_file = f.read()

input_data = [(line.split()[0], int(line.split()[1])) for line in input_file.splitlines()]

# print(input_data)

head_pos: list[int, int] = [0, 0]
tail_pos: list[int, int] = [0, 0]
tail_visited_pos: set[tuple[int, int]] = set()
tail_visited_pos.add((0, 0))

for movement in input_data:
    move_head(movement)

print("Solution:", len(tail_visited_pos))
