seconds_first = int(input())
seconds_second = int(input())
seconds_third = int(input())

total_seconds = seconds_first + seconds_second + seconds_third  # 121
minutes = total_seconds // 60  # 121 // 60 == 2
seconds = total_seconds % 60  # 121 % 60 == 1

print(f'{minutes}:{seconds :02d}')
