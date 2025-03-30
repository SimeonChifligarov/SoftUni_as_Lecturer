width = int(input())
length = int(input())
height = int(input())

total_space = width * length * height

command = input()  # 'Done', OR taken_space_as_str , e.g. '13'
while command != 'Done':
    boxes = int(command)
    total_space -= boxes

    if total_space <= 0:
        break

    command = input()

is_free_space = total_space > 0

if is_free_space:
    print(f'{total_space} Cubic meters left.')
else:
    print(f'No more free space! You need {-total_space} Cubic meters more.')
