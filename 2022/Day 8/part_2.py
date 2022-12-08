def get_row_split(y_coord: int, split_at_x: int):
    row = data_array[y_coord]
    return [row[:split_at_x], row[split_at_x + 1:]]


def get_column_split(x_coord: int, split_at_y: int):
    global input_height
    column: list[int] = []
    for y_coord in range(input_height):
        column.append(data_array[y_coord][x_coord])
    return [column[:split_at_y], column[split_at_y + 1:]]


def calc_scenic_score(x_coord: int, y_coord: int):
    tree_height = data_array[y_coord][x_coord]
    scenic_left = 0
    scenic_right = 0
    scenic_up = 0
    scenic_down = 0
    rows = get_row_split(y_coord, x_coord)
    columns = get_column_split(x_coord, y_coord)

    for normal_array in (rows[1], columns[1]):
        if len(normal_array) != 0:
            for index in range(len(normal_array)):
                if index == len(normal_array) - 1:
                    if normal_array in rows:
                        scenic_right = len(normal_array)
                        break
                    else:
                        scenic_down = len(normal_array)
                        break
                tree = normal_array[index]
                if tree >= tree_height:
                    if normal_array in rows:
                        scenic_right = index + 1
                        break
                    else:
                        scenic_down = index + 1
                        break
    for reversed_array in (rows[0], columns[0]):
        if len(reversed_array) != 0:
            for index in range(len(reversed_array)):
                if index == len(reversed_array) - 1:
                    if reversed_array in rows:
                        scenic_left = len(reversed_array)
                        break
                    else:
                        scenic_up = len(reversed_array)
                        break
                tree = reversed_array[-(index + 1)]
                if tree >= tree_height:
                    if reversed_array in rows:
                        scenic_left = index + 1
                        break
                    else:
                        scenic_up = index + 1
                        break

    return scenic_up * scenic_right * scenic_down * scenic_left


with open('input') as f:
    input_data = f.read()

# input_data = '''30373
# 25512
# 65332
# 33549
# 35390
# '''

input_array = input_data.splitlines()

input_width = len(input_array[0])
input_height = len(input_array)

data_array: list[list[int]] = []

for j in range(len(input_array)):
    data_array.append([int(num) for num in input_array[j]])

# print(data_array)

# score, x_coord, y_coord
highest_score = [0, 0, 0]

# calc_scenic_score(2, 1)

for y in range(1, input_height - 1):
    for x in range(1, input_width - 1):
        if (score := calc_scenic_score(x, y)) > highest_score[0]:
            highest_score = [score, x, y]

print(f'Solution: Highest score of {highest_score[0]} at {highest_score[1]}:{highest_score[2]}')
