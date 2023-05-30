width = int(input())
length = int(input())
height = int(input())

total_space = width * length * height

left_space = total_space

command = input()  # "Done" OR integer as string, e.g. "13", "22", ...
while command != "Done":
    current_box = int(command)
    left_space -= current_box
    if left_space <= 0:  # has value of non-positive, e.g. "-22"
        break

    command = input()

if command == "Done":
    print(f"{left_space} Cubic meters left.")
else:
    print(f"No more free space! You need {-left_space} Cubic meters more.")  # e.g. "-22" => "22"
