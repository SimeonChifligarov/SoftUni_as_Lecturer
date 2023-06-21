# 03. Stream Of Letters from More Exercises
c_count = 0
o_count = 0
n_count = 0

result_string = ""
current_string = ""

command = input()

while not command == "End":
    if not command.isalpha():
        command = input()
        continue

    if command == "c":
        if c_count == 1:
            current_string += command
        elif c_count == 0:
            c_count += 1
            if c_count == 1 and o_count == 1 and n_count == 1:
                c_count = 0
                o_count = 0
                n_count = 0
                result_string += f"{current_string} "
                current_string = ""
                command = input()
                continue
            command = input()
            continue
    elif command == "n":
        if n_count == 1:
            current_string += command
        elif n_count == 0:
            n_count += 1
            if c_count == 1 and o_count == 1 and n_count == 1:
                c_count = 0
                o_count = 0
                n_count = 0
                result_string += f"{current_string} "
                current_string = ""
                command = input()
                continue
            command = input()
            continue
    elif command == "o":
        if o_count == 1:
            current_string += command
        elif o_count == 0:
            o_count += 1
            if c_count == 1 and o_count == 1 and n_count == 1:
                c_count = 0
                o_count = 0
                n_count = 0
                result_string += f"{current_string} "
                current_string = ""
                command = input()
                continue
            command = input()
            continue
    else:
        current_string += command

    command = input()

print(result_string)
