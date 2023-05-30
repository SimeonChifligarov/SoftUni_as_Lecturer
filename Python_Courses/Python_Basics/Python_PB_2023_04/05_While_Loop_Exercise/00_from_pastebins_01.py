DONE_COMMAND = "Done"

space_width = int(input())
space_length = int(input())
space_height = int(input())

space_total = space_width * space_length * space_height

space_not_occupied = space_total
while True:
    command = input()  # "Done" OR "12"
    if command == DONE_COMMAND:
        break

    current_boxes = int(command)  # "12"
    space_not_occupied -= current_boxes  # 120 - "12"
    if space_not_occupied <= 0:
        break

if space_not_occupied > 0:
    print(f"{space_not_occupied} Cubic meters left.")
else:
    print(f"No more free space! You need {-space_not_occupied} Cubic meters more.")
