import sys

min_number = sys.maxsize

command = input()
while not command == "Stop":
    number = int(command)
    if number < min_number:
        min_number = number

    command = input()

print(min_number)
