class Command:
    def __init__(self):
        self.name = None
        self.arg = None
        self.output = None

    def __str__(self):
        return f"Name: {self.name}\nArgument: {self.arg}\nOutput: {self.output}\n"


class File:
    def __init__(self, name, size):
        self.name: str = name
        self.size: int = size

    def __str__(self):
        return f"{self.name} (file, size={self.size})"


class Directory:
    def __init__(self, name):
        self.name: str = name
        self.children: [Directory or File] = []

    def __str__(self):
        return f"{self.name} (dir)"


# def get_dir_from_path(path):
#     global root_dir
#     current_dir = root_dir
#     if len(path) == 0:
#         return root_dir
#     for path_element in path:
#         children_of_current_dir = current_dir.children
#         if len(children_of_current_dir) == 0:
#             print('Has no children')
#             exit(-1)
#         for element in children_of_current_dir:
#             if isinstance(element, Directory) and element.name == path_element:
#                 return element
#             else:
#                 print("Directory non existent")
#                 exit(-1)


def get_dir_from_path(path: list):
    global root_dir
    current_dir = root_dir
    if len(path) == 0:
        return root_dir
    if path[0] == '/':
        if len(path) == 1:
            return root_dir
        path.pop(0)
    for path_element in path:
        children_of_current_dir = current_dir.children
        if len(children_of_current_dir) == 0:
            print('Has no children')
            exit(-1)
        for element in children_of_current_dir:
            if isinstance(element, Directory) and element.name == path_element:
                current_dir = element
            # else:
            #     print("Directory non existent")
            #     exit(-1)
    return current_dir


def print_file_tree(dir_to_print: list):
    current_dir = get_dir_from_path(dir_to_print)
    if len(dir_to_print) == 0:
        print(f'- {str(current_dir)}')
    depth = len(dir_to_print) + 1
    for child in current_dir.children:
        if isinstance(child, Directory):
            print(f'{"  " * depth}- {str(child)}')
            dir_to_print.append(child.name)
            assert isinstance(dir_to_print, list)
            print_file_tree(dir_to_print)
        else:
            print(f'{"  " * depth}- {str(child)}')


with open('input') as f:
    input_data = f.read()

raw_commands = input_data.split('$ ')
raw_commands.pop(0)
# print(raw_commands)

commands = []

file_tree = {}
directory_pointer = {}

for i in range(len(raw_commands)):
    command = raw_commands[i]
    current_command = Command()
    command_lines = command.splitlines()
    if len(command_lines[0].split()) == 1:
        current_command.name = command_lines[0].split()[0]
    else:
        current_command.name, current_command.arg = command_lines[0].split()

    if len(command_lines) > 1:
        current_command.output = command_lines[1:]
    if current_command.name is None:
        print(f'Command without name: {current_command}')
        exit(-1)

    commands.append(current_command)

root_dir = Directory("/")

current_path = []

# print(commands[1])

for command in commands:
    if command.name == "cd":
        if command.arg == "/":
            current_path = []
        elif command.arg == "..":
            current_path.pop()
        else:
            current_path.append(command.arg)
    if command.name == "ls":
        for element in command.output:
            output_parts = element.split()
            if output_parts[0] == "dir":
                get_dir_from_path(current_path).children.append(Directory(output_parts[1]))
            else:
                get_dir_from_path(current_path).children.append(File(output_parts[1], output_parts[0]))

print_file_tree([])
