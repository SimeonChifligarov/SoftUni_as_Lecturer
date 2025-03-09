# 1. E
first_seconds = int(input())
second_seconds = int(input())
third_seconds = int(input())

# 2. T
sum_seconds = first_seconds + second_seconds + third_seconds  # 121  => 2:01

total_minutes = sum_seconds // 60  # 121 // 60 == 2
total_seconds = sum_seconds % 60  # 121 % 60 == 1
# total_seconds = sum_seconds - total_minutes * 60  # 121 - 2 * 60 == 121 - 120 == 1

# 3. L
# if total_seconds >= 10:
#     print(f'{total_minutes}:{total_seconds}')
# else:  # elif total_seconds <= 9:  # elif total_seconds < 10:
#     print(f'{total_minutes}:0{total_seconds}')

print(f'{total_minutes}:{total_seconds:02d}')
