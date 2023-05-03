import math

serial_name = input()
serial_time = float(input())
total_break_time = float(input())

lunch_time = total_break_time * (1 / 8)
relax_time = total_break_time * (1 / 4)

rest_time = total_break_time - lunch_time - relax_time
needed_time = serial_time - rest_time

if rest_time >= serial_time:
    print(f"You have enough time to watch {serial_name} and left with {math.ceil(-needed_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {math.ceil(needed_time)} more minutes.")
