width = int(input())
length = int(input())
height = int(input())

total_space = width * length * height

while True:
    command = input()  # 'Done' or boxes_as_str

    if command == 'Done':
        break

    boxes = int(command)
    total_space -= boxes

    if total_space <= 0:
        break

is_free_space = total_space > 0

if is_free_space:
    print(f'{total_space} Cubic meters left.')
else:
    print(f'No more free space! You need {-total_space} Cubic meters more.')
