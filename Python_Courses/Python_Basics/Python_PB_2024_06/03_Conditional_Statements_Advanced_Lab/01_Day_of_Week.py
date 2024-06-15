day_of_week = int(input())  # int('3') == 3

result = ''

if day_of_week == 1:
    result = 'Monday'
elif day_of_week == 2:
    result = 'Tuesday'
elif day_of_week == 3:
    result = 'Wednesday'
elif day_of_week == 4:
    result = 'Thursday'
elif day_of_week == 5:
    result = 'Friday'
elif day_of_week == 6:
    result = 'Saturday'
elif day_of_week == 7:
    result = 'Sunday'
else:
    result = 'Error'

print(result)
