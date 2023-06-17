GREEN_PAINT_M2_PER_LITER = 3.4
RED_PAINT_M2_PER_LITER = 4.3

house_height = float(input())
house_length = float(input())
roof_height = float(input())

side_wall_area = house_height * house_length
window_area = 1.5 * 1.5

side_walls_paint_area = 2 * (side_wall_area - window_area)

front_door_area = 2 * 1.2
back_wall_area = house_height * house_height
front_wall_area = house_height * house_height - front_door_area

total_green_paint_area = side_walls_paint_area + back_wall_area + front_wall_area
total_green_paint_needed = total_green_paint_area / GREEN_PAINT_M2_PER_LITER

print(f"{total_green_paint_needed :.2f}")

roof_rectangle = house_height * house_length
roof_triangle = house_height * roof_height / 2

roof_area = 2 * (roof_rectangle + roof_triangle)
total_red_paint_area = roof_area

total_red_paint_needed = total_red_paint_area / RED_PAINT_M2_PER_LITER

print(f"{total_red_paint_needed :.2f}")
