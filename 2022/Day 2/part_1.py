from time import process_time_ns

with open("input") as f:
    input_data = f.read()


def is_win(opponent, me):
    if me == 'R' and opponent == 'S':
        return 1
    elif me == 'S' and opponent == 'P':
        return 1
    elif me == 'P' and opponent == 'R':
        return 1

    if me == 'S' and opponent == 'R':
        return 0
    elif me == 'P' and opponent == 'S':
        return 0
    elif me == 'R' and opponent == 'P':
        return 0

    else:
        return -1


games = [i.split(' ') for i in input_data.splitlines()]
print(games)
for index in range(len(games)):
    game = games[index]
    opponent = game[0]
    me = game[1]

    if opponent == 'A':
        game[0] = 'R'
    elif opponent == 'B':
        game[0] = 'P'
    else:
        game[0] = 'S'

    if me == 'X':
        game[1] = 'R'
    elif me == 'Y':
        game[1] = 'P'
    else:
        game[1] = 'S'

print(games)

scores = []
for index in range(len(games)):
    game = games[index]
    gameScore = 0

    if game[1] == 'R':
        gameScore += 1
    elif game[1] == 'P':
        gameScore += 2
    else:
        gameScore += 3

    isWin = is_win(*game)
    if isWin == -1:
        gameScore += 3
    elif isWin == 1:
        gameScore += 6

    scores.append(gameScore)

print(scores)
print('Total Score: ' + str(sum(scores)))

print('Process took', process_time_ns(), 'nanoseconds')
