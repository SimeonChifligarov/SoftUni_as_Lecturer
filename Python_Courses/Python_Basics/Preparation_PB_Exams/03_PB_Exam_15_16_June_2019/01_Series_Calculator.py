import math

ADVERTISEMENTS_PERCENT = 0.20
SPECIAL_EPISODE_EXTRA = 10

series_name = input()
seasons_count = int(input())
episodes_count = int(input())
episode_length = float(input())

total_time = seasons_count * episodes_count * episode_length * (1 + ADVERTISEMENTS_PERCENT) \
             + seasons_count * SPECIAL_EPISODE_EXTRA

print(f"Total time needed to watch the {series_name} series is {math.floor(total_time)} minutes.")
