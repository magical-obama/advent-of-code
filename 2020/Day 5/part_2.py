def get_row(row_str):
    row = []
    for i in range(128):
        row.append(i)
    for char in row_str:
        row_len_half = int(len(row)/2)
        if char == "F":
            row[row_len_half:] = []
        elif char == "B":
            row[:row_len_half] = []
    return int(row[0])

def get_seat(seat_str):
    seat = []
    for i in range(8):
        seat.append(i)
    for char in seat_str:
        seat_len_half = int(len(seat)/2)
        if char == "L":
            seat[seat_len_half:] = []
        elif char == "R":
            seat[:seat_len_half] = []
    return int(seat[0])

def get_id(row, seat):
    return int(row * 8 + seat)

# Functions End

f = open("input.txt", "r")
bPasses = f.read().split("\n")

for i in range(len(bPasses)):
    bPasses[i] = [bPasses[i], [bPasses[i][:7], bPasses[i][7:]]]

# for i in range(len(bPasses)):
#     print("Pass Nr:", i)
#     print("Row:\t", get_row(bPasses[i][1][0]))
#     print("Seat:\t", get_seat(bPasses[i][1][1]))
#     print("ID:\t", get_id(get_row(bPasses[i][1][0]), get_seat(bPasses[i][1][1])))
#     print()

highestId = 0
allIds = []
for i in range(len(bPasses)):
    currentId = get_id(get_row(bPasses[i][1][0]), get_seat(bPasses[i][1][1]))
    allIds.append(int(currentId))
    if currentId >= highestId:
        highestId = currentId

allIds.sort()

for i in range(allIds[0], allIds[-1]):
    x = i - allIds[0]
    if allIds[x] != i:
        print("My Seat:", i)
        break

print("Highest ID:", highestId)

# Link: https://adventofcode.com/2020/day/5#part2
# Antwort: 625