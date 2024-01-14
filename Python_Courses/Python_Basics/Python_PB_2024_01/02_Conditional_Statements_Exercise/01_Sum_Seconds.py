seconds_first = int(input())
seconds_second = int(input())
seconds_third = int(input())

seconds_sum = seconds_first + seconds_second + seconds_third

total_min = seconds_sum // 60  # 125 // 60 => 2
total_sec = seconds_sum % 60  # 125 % 60 == 5

# if total_sec >= 10:
#     print(f'{total_min}:{total_sec}')
# else:  # i.e. total_sec < 10, i.e. {0, 1, 2, ... 9}
#     print(f'{total_min}:0{total_sec}')

print(f'{total_min}:{total_sec:02d}')
