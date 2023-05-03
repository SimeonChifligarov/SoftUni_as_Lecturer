# ### version 1.0
# current_hour = int(input())
# current_minute = int(input())
#
# current_time_in_minutes = current_hour * 60 + current_minute + 15
#
# current_time_as_hour = current_time_in_minutes // 60
# if current_time_as_hour == 24:
#     current_time_as_hour = 0
#
# current_time_as_minutes = current_time_in_minutes % 60
#
# print(f"{current_time_as_hour}:{current_time_as_minutes:02d}")


# ### version 2.0
current_hour = int(input())
current_minute = int(input())

current_minute_plus_15 = current_minute + 15
if current_minute_plus_15 >= 60:
    current_minute_plus_15 -= 60
    current_hour += 1

if current_hour == 24:
    current_hour = 0

print(f"{current_hour}:{current_minute_plus_15:02d}")
