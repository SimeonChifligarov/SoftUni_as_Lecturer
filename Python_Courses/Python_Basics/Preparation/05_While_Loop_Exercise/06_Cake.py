STOP_COMMAND = "STOP"

cake_width = int(input())
cake_length = int(input())

cake_pieces = cake_width * cake_length

while True:
    command = input()
    if command == STOP_COMMAND:
        break

    current_pieces = int(command)
    cake_pieces -= current_pieces
    if cake_pieces <= 0:
        break

if cake_pieces > 0:
    print(f"{cake_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {-cake_pieces} pieces more.")
