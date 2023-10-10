import math

series = input()
episode_length = int(input())
break_length = int(input())

lunch_length = break_length / 8
rest_length = break_length / 4

time_needed = lunch_length + rest_length + episode_length

if time_needed <= break_length:  # happy case
    time_left = math.ceil(break_length - time_needed)
    print(f"You have enough time to watch {series} and left with {time_left} minutes free time.")
else:  # unhappy case
    time_not_enough = math.ceil(time_needed - break_length)
    print(f"You don't have enough time to watch {series}, you need {time_not_enough} more minutes.")
