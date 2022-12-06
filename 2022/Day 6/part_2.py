input_data = ""
buf_len = 14


with open('input') as f:
    input_data = f.read()


def advance_buffer():
    global current_index
    if len(buf) < buf_len:
        buf.append(input_data[current_index])
    else:
        buf.pop(0)
        buf.append(input_data[current_index])
    current_index += 1


def process_next():
    if len(buf) < buf_len:
        advance_buffer()
    else:
        if len(set(buf)) == len(buf):
            return True
        advance_buffer()
    return False

buf = []
current_index = 0
for i in range(len(input_data)):
    if process_next():
        print('Solution:', current_index)
        break
