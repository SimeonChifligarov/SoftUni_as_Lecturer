hours = int(input())
minutes = int(input())

minutes_plus_15 = minutes + 15

if minutes_plus_15 >= 60:  # 65 -> 5; +1h
    minutes_plus_15 -= 60  # minutes_plus_15 = minutes_plus_15 - 60
    hours += 1  # hours = hours + 1

if hours == 24:
    hours = 0

print(f'{hours}:{minutes_plus_15 :02d}')
