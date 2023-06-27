import math

TIRED_COMMAND = "Tired!"
WALLS_COUNT = 4

wall_height = int(input())
wall_width = int(input())
percent_occupied = int(input()) / 100

total_paint_area = math.ceil(wall_height * wall_width * WALLS_COUNT * (1 - percent_occupied))
current_paint_area = 0

is_success = False
command = input()
while command != TIRED_COMMAND:
    paint_liters = int(command)
    current_paint_area += paint_liters
    if current_paint_area >= total_paint_area:
        is_success = True
        break

    command = input()

if is_success:
    diff = current_paint_area - total_paint_area
    if diff > 0:
        print(f"All walls are painted and you have {diff} l paint left!")
    else:  # elif diff == 0:
        print("All walls are painted! Great job, Pesho!")
else:
    print(f"{total_paint_area - current_paint_area} quadratic m left.")
