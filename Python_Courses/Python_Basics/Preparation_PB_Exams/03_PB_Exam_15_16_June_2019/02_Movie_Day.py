PREPARATION_PERCENT = 15 / 100

filming_time = int(input())
scenes_count = int(input())
scene_length = int(input())

needed_time = scenes_count * scene_length
actual_time = filming_time * (1 - PREPARATION_PERCENT)

if actual_time >= needed_time:
    print(f"You managed to finish the movie on time! You have {round(actual_time - needed_time)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(needed_time - actual_time)} minutes.")
