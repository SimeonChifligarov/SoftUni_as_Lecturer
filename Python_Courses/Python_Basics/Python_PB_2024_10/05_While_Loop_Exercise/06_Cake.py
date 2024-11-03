cake_length = int(input())
cake_width = int(input())

cake_pieces = cake_length * cake_width

command = input()  # 'STOP' or pieces as a str (e.g. '20')
while command != 'STOP':
    pieces = int(command)

    cake_pieces -= pieces
    if cake_pieces <= 0:
        break

    command = input()  # change

if cake_pieces >= 0:
    print(f'{cake_pieces} pieces are left.')
else:
    print(f'No more cake left! You need {-cake_pieces} pieces more.')
