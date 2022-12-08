def get_row(y_coord: int):
    return data_array[y_coord]


def get_column(x_coord: int):
    global input_height
    output: list[int] = []
    for y_coord in range(input_height):
        output.append(data_array[y_coord][x_coord])
    return output


def is_highest(list_to_check: list[int], height_to_check: int):
    if max(list_to_check) < height_to_check:
        return True
    else:
        return False


def is_visible(x_coord: int, y_coord: int):
    tree_height = data_array[y_coord][x_coord]
    # print(tree_height)
    tree_visible = False
    tree_row = get_row(y_coord)
    # print(tree_row)
    tree_rows = [tree_row[:x_coord], tree_row[x_coord + 1:]]

    tree_column = get_column(x_coord)
    tree_columns = [tree_column[:y_coord], tree_column[y_coord + 1:]]
    for to_check in (tree_rows[0], tree_rows[1], tree_columns[0], tree_columns[1]):
        if is_highest(to_check, tree_height):
            tree_visible = True
    return tree_visible


with open('input') as f:
    input_data = f.read()

input_array = input_data.splitlines()

input_width = len(input_array[0])
input_height = len(input_array)

data_array: list[list[int]] = []

for j in range(len(input_array)):
    data_array.append([int(num) for num in input_array[j]])

# print(input_array)

trees_visible = 0

trees_visible += input_width * 2
trees_visible += (input_height - 2) * 2


for y in range(1, input_height - 1):
    for x in range(1, input_width - 1):
        if is_visible(x, y):
            trees_visible += 1
#
print('Solution:', trees_visible)
