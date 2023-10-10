seconds_first = int(input())
seconds_second = int(input())
seconds_third = int(input())

total_seconds = seconds_first + seconds_second + seconds_third

minutes = total_seconds // 60  # 125 => 2           125 // 60 => 2   120 // 60 => 2
seconds = total_seconds % 60   # 125 => 5

print(f"{minutes}:{seconds :02d}")
