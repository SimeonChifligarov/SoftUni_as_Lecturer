width = int(input())
length = int(input())
height = int(input())

total_space_left = width * length * height

while True:
    command = input()  # 'Done' or space as a string

    if command == 'Done':
        break

    space = int(command)  # e.g. int('20') == 20

    total_space_left -= space
    if total_space_left <= 0:
        break

is_space_left = total_space_left >= 0
if not is_space_left:
    print(f'No more free space! You need {-total_space_left} Cubic meters more.')
else:
    print(f'{total_space_left} Cubic meters left.')
