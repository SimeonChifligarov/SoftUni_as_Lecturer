# 1.
hours = int(input())
minutes = int(input())

# 2.
minutes_plus_15 = minutes + 15
total_minutes = hours * 60 + minutes_plus_15

new_hours = total_minutes // 60  #
if new_hours >= 24:
    new_hours = 0

new_minutes = total_minutes % 60

# 3.
print(f'{new_hours}:{new_minutes:02d}')
