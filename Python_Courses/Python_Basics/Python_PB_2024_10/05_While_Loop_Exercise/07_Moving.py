width = int(input())
length = int(input())
height = int(input())

total_space = width * length * height

# 4.	На следващите редове (до получаване на команда "Done") - брой кашони, които се пренасят в квартирата - цели числа
command = input()  # 'Done' or spaces as a str (e.g. '10')
while command != 'Done':
    spaces = int(command)

    total_space -= spaces
    if total_space <= 0:
        break

    command = input()

if total_space >= 0:
    print(f'{total_space} Cubic meters left.')
else:
    print(f'No more free space! You need {-total_space} Cubic meters more.')
