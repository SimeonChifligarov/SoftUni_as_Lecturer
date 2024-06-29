# която до получаване на командата "Stop", чете цели числа
import sys

max_number = -sys.maxsize

command = input()  # "Stop" or "13"
while command != "Stop":
    current_number = int(command)  # int('13') == 13
    if current_number > max_number:
        max_number = current_number

    command = input()

print(max_number)
