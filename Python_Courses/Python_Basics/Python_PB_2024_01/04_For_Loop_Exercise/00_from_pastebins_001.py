exam_hour = int(input()) * 60
exam_min = int(input()) + exam_hour
arrive_hour = int(input()) * 60
arrive_min = int(input()) + arrive_hour

the_time = exam_min - arrive_min
if the_time < 0:
    the_time = abs(the_time)
the_hours = the_time // 60
the_minutes = the_time % 60

if arrive_min > exam_min:  # ---------------------Late--------------------
    if the_time > 59:
        print(f'Late')
        print(f'{the_hours}:{the_minutes:02d} hours after the start')
    else:
        print(f'Late')
        print(f'{the_time} minutes after the start')
elif the_time <= 30:  # ---------------------------On time----------------
    if exam_min == arrive_min:
        print(f'On time')
    else:
        print(f'On time')
        print(f'{the_time} minutes before the start')
elif the_time >= 31:  # ---------------------------Early------------------
    if the_time > 59:
        print(f'Early')
        print(f'{the_hours}:{the_minutes:02d} hours before the start')
    else:
        print(f'Early')
        print(f'{the_time} minutes before the start')