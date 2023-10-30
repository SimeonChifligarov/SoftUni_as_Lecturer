width = int(input())
length = int(input())
height = int(input())

space_total = width * length * height
space_left = space_total

command = input()  # "Done" OR integer as string, e.g. "7"
while command != "Done":
    current_boxes = int(command)  # e.g. int("7") == 7
    space_left -= current_boxes
    if space_left <= 0:
        break

    command = input()

if command == "Done":
    print(f"{space_left} Cubic meters left.")
else:
    space_needed = -space_left
    print(f"No more free space! You need {space_needed} Cubic meters more.")
