width = int(input())
length = int(input())

cake_pieces = width * length
cake_pieces_left = cake_pieces
is_cake_left = True

command = input()  # either 'STOP', or current_pieces as string, e.g. '20'
while command != 'STOP':
    current_pieces = int(command)
    cake_pieces_left -= current_pieces
    if cake_pieces_left < 0:
        is_cake_left = False
        break

    command = input()

if is_cake_left:
    print(f'{cake_pieces_left} pieces are left.')
else:
    print(f'No more cake left! You need {-cake_pieces_left} pieces more.')
