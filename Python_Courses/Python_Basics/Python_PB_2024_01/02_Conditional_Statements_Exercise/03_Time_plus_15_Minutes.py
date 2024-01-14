current_hour = int(input())
current_min = int(input())

current_min_plus_15 = current_min + 15

if current_min_plus_15 >= 60:
    # current_min_plus_15 = current_min_plus_15 - 60
    current_min_plus_15 -= 60
    # current_hour = current_hour + 1
    current_hour += 1

if current_hour >= 24:
    current_hour = 0

print(f'{current_hour}:{current_min_plus_15:02d}')
