DONE_COMMAND = "Done"

space_width = int(input())
space_length = int(input())
space_height = int(input())

space_total = space_width * space_length * space_height

space_not_occupied = space_total
while True:
    command = input()
    if command == DONE_COMMAND:
        break

    current_boxes = int(command)
    space_not_occupied -= current_boxes
    if space_not_occupied <= 0:
        break

if space_not_occupied > 0:
    print(f"{space_not_occupied} Cubic meters left.")
else:
    print(f"No more free space! You need {-space_not_occupied} Cubic meters more.")
