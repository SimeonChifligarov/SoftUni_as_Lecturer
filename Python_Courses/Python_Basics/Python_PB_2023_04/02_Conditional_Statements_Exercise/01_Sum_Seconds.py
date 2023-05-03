seconds_first = int(input())
seconds_second = int(input())
seconds_third = int(input())

seconds_sum = seconds_first + seconds_second + seconds_third
# print(seconds_sum)

seconds_sum_as_minutes = seconds_sum / 60  # int(seconds_sum / 60)
seconds_sum_as_seconds = seconds_sum % 60

print(f"{seconds_sum_as_minutes}:{seconds_sum_as_seconds :02d}")
