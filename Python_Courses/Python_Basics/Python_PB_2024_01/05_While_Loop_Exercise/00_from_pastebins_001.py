width = int(input())
length = int(input())

cake_pieces = width * length
cake_pieces_left = cake_pieces

command = input()

while command != 'STOP':
    current_pieces = int(command)
    cake_pieces_left -= current_pieces
    if cake_pieces_left <= 0:
        break

    command = input()

if command == 'STOP':
    print(f'{cake_pieces_left} pieces are left.')

else:
    print(f'No more cake left! You need {-cake_pieces_left} pieces more.')
