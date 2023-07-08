capacity = float(input())

available_space = capacity
luggage_count = 0
is_full = False

command = input()
while command != "End":
    luggage_count += 1
    luggage = float(command)

    if luggage_count % 3 == 0:
        luggage *= (1 + 0.10)

    available_space -= luggage
    if available_space < 0:
        luggage_count -= 1
        is_full = True
        break

    command = input()

if is_full:
    print("No more space!")
else:
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {luggage_count} suitcases loaded.")
