seconds_first = int(input())
seconds_second = int(input())
seconds_third = int(input())

seconds_sum = seconds_first + seconds_second + seconds_third

minutes_of_seconds_sum = seconds_sum // 60
seconds_of_seconds_sum = seconds_sum % 60

print(f"{minutes_of_seconds_sum}:{seconds_of_seconds_sum:02d}")
