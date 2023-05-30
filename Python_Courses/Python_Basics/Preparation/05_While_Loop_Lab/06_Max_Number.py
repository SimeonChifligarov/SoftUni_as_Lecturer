import sys

max_number = -sys.maxsize

command = input()
while not command == "Stop":
    number = int(command)
    if number > max_number:
        max_number = number

    command = input()

print(max_number)
