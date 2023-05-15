prices_by_day = {
    "Monday": 12,
    "Tuesday": 12,
    "Wednesday": 14,
    "Thursday": 14,
    "Friday": 12,
    "Saturday": 16,
    "Sunday": 16,
}

weekday = input()
price = prices_by_day[weekday]

print(price)
