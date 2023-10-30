cake_width = int(input())
cake_length = int(input())

cake_pieces_total = cake_width * cake_length
cake_pieces_left = cake_pieces_total

# is_cake_done = False
command = input()  # "STOP" OR integer as string, i.e. "13"
while command != "STOP":
    current_pieces = int(command)
    cake_pieces_left -= current_pieces
    if cake_pieces_left <= 0:
        break

    command = input()

if command == "STOP":
    print(f"{cake_pieces_left} pieces are left.")
else:
    cake_pieces_needed = -cake_pieces_left
    print(f"No more cake left! You need {cake_pieces_needed} pieces more.")
