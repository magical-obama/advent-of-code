def run_actions(input_list):
    num = 0
    i = 0
    done = []
    while i <= len(input_list):
        if done.count(i) == 1:
            # print(i)
            return [False, num, done]
        if i == len(input_list) + 1:
            return [True, num, done]
        done.append(i)
        if input_list[i][1][0] == "acc":
            if input_list[i][1][1][0] == "+":
                num += int(input_list[i][1][1][1:])
            # elif input_list[i][1][1][0] == "-":
            #     num -= int(input_list[i][1][1][1:])
            else:
                num -= int(input_list[i][1][1][1:])
        if input_list[i][1][0] == "jmp":
            if input_list[i][1][1][0] == "+":
                i += int(input_list[i][1][1][1:])
            else:
                i -= int(input_list[i][1][1][1:])
            # elif input_list[i][1][1][0] == "-":
            #     i -= int(input_list[i][1][1][1:])
            continue

        i += 1
    return [False, num, done]

f = open("input.txt", "r")
lines = f.read().split("\n")


for i in range(len(lines)):
    lines[i] = [lines[i], lines[i].split()]

# print(run_actions(lines))

last_changed = 0
found = False
while run_actions(lines)[0] != True:
    # print(run_actions(lines)[1])
    for x in range(last_changed, len(lines)):
        if lines[x][1][0] == "jmp":
            lines[x][1][0] = "nop"
            last_changed = x + 1
            # print("Correct jmp")
            break
        elif lines[x][1][0] == "nop":
            lines[x][1][0] = "jmp"
            last_changed = x + 1
            # print("Correct nop")
            break
        # else:
        #     print("Error")
        #     print(x)
    # last_run = run_actions(lines)

print(run_actions(lines)[1])