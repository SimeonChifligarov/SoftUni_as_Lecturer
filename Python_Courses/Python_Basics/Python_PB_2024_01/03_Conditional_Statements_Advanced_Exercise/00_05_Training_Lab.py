hallway = 100
desk_size = 70
row_size = 120
door_size_as_desks = 3

length = float(input()) * 100
height = float(input()) * 100

useful_height = height - hallway

desks_per_row = int(useful_height / desk_size)
rows = int(length / row_size)

desks = int(rows * desks_per_row - door_size_as_desks)
print(desks)
