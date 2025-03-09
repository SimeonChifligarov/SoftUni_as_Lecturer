# 1.
hours = int(input())
minutes = int(input())

# 2.
minutes += 15  # minutes = minutes + 15
if minutes >= 60:  # 71
    minutes -= 60  # 11
    hours += 1  # 1 -> 2

if hours >= 24:
    hours = 0

# 3.
print(f'{hours}:{minutes:02d}')
