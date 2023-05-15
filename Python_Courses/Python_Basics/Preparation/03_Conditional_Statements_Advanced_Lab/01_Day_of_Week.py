# # Solution 1
# day_of_the_week = input()
#
# print_day = ""
# if day_of_the_week == "1":
#     print_day = "Monday"
# elif day_of_the_week == "2":
#     print_day = "Tuesday"
# elif day_of_the_week == "3":
#     print_day = "Wednesday"
# elif day_of_the_week == "4":
#     print_day = "Thursday"
# elif day_of_the_week == "5":
#     print_day = "Friday"
# elif day_of_the_week == "6":
#     print_day = "Saturday"
# elif day_of_the_week == "7":
#     print_day = "Sunday"
# else:
#     print_day = "Error"
#
# print(print_day)

# Solution 2
week_days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

day_of_the_week_idx = int(input()) - 1

if day_of_the_week_idx in range(len(week_days)):
    print(week_days[day_of_the_week_idx])
else:
    print("Error")
