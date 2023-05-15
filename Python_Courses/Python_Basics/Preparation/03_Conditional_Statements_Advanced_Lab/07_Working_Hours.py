working_days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
]

non_working_days = [
    "Sunday",
]

hour = int(input())
weekday = input()

if weekday in working_days and 10 <= hour <= 18:
    print("open")
else:
    print("closed")
