# Done

width = int(input())
length = int(input())
height = int(input())

total_spaces = width * length * height

while True:
    command = input()  # 'Done' or spaces as a str

    if command == 'Done':
        break

    current_spaces = int(command)
    total_spaces -= current_spaces
    if total_spaces <= 0:
        break

if total_spaces >= 0:
    print(f'{total_spaces} Cubic meters left.')
else:
    print(f'No more free space! You need {-total_spaces} Cubic meters more.')
