cake_width = int(input())
cake_length = int(input())

cake_total_pieces = cake_width * cake_length

command = input()  # 'STOP' or pieces as a string, e.g. '20'
while command != 'STOP':
    current_pieces = int(command)  # e.g. int('20') == 20

    cake_total_pieces -= current_pieces

    if cake_total_pieces <= 0:
        break

    command = input()

is_cake_left = cake_total_pieces > 0
if is_cake_left:
    print(f'{cake_total_pieces} pieces are left.')
else:
    print(f'No more cake left! You need {-cake_total_pieces} pieces more.')
