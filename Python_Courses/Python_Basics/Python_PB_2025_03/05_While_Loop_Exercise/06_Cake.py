cake_width = int(input())
cake_length = int(input())

cake_pieces = cake_width * cake_length

command = input()  # 1. init  # 'STOP', OR current_pieces_as_str
while command != 'STOP':  # 2. check condition
    current_pieces = int(command)  # int('20') == 20
    cake_pieces -= current_pieces

    if cake_pieces <= 0:
        break

    command = input()  # 3. potential change

is_cake_enough = cake_pieces >= 0

if is_cake_enough:
    print(f'{cake_pieces} pieces are left.')
else:
    print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')  # -(-1) == 1
