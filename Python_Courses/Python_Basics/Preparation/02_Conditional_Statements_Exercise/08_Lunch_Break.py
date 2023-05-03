import math

LUNCH_TIME_AS_MULTIPLIER = 1 / 8
REST_TIME_AS_MULTIPLIER = 1 / 4

movie_series = input()
episode_length = int(input())
break_length = int(input())

break_extra_length = (1 - (LUNCH_TIME_AS_MULTIPLIER + REST_TIME_AS_MULTIPLIER)) * break_length

if break_extra_length >= episode_length:
    print(f"You have enough time to watch {movie_series} "
          f"and left with {math.ceil(break_extra_length - episode_length)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_series}, "
          f"you need {math.ceil(episode_length - break_extra_length)} more minutes.")
