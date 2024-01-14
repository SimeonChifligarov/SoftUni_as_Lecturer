from math import ceil

series = input()
series_length = int(input())
break_length = int(input())

# Времето за обяд ще бъде 1/8 от времето за почивка,
lunch_duration = break_length * 1 / 8
# времето за отдих ще бъде 1/4 от времето за почивка.
rest_duration = break_length * 1 / 4

time_remaining = break_length - (lunch_duration + rest_duration)

if time_remaining >= series_length:
    time_left = time_remaining - series_length
    print(f'You have enough time to watch {series} and left with {ceil(time_left)} minutes free time.')
else:
    time_needed = series_length - time_remaining
    print(f'You don\'t have enough time to watch {series}, you need {ceil(time_needed)} more minutes.')
