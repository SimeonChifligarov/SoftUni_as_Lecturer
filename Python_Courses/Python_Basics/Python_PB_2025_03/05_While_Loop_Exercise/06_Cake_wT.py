cake_width = int(input())
cake_length = int(input())

cake_pieces = cake_width * cake_length

while True:
    command = input()  # 'STOP' or current_pieces_as_str

    if command == 'STOP':
        break

    current_pieces = int(command)  # e.g. int('13') == 13
    cake_pieces -= current_pieces

    if cake_pieces <= 0:
        break

is_cake_enough = cake_pieces >= 0

if is_cake_enough:
    print(f'{cake_pieces} pieces are left.')
else:
    print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')  # -(-1) == 1
