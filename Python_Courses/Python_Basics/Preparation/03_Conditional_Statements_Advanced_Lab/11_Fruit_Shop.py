week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
weekends = ("Saturday", "Sunday")

fruit = input()
weekday = input()
fruit_quantity = float(input())
fruit_price = 0

if fruit not in ("banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes") \
        or weekday not in (week_days + weekends):
    print("error")
elif fruit == "banana" and weekday in week_days:
    fruit_price = 2.50
elif fruit == "banana" and weekday in weekends:
    fruit_price = 2.70
elif fruit == "apple" and weekday in week_days:
    fruit_price = 1.20
elif fruit == "apple" and weekday in weekends:
    fruit_price = 1.25
elif fruit == "orange" and weekday in week_days:
    fruit_price = 0.85
elif fruit == "orange" and weekday in weekends:
    fruit_price = 0.90
elif fruit == "grapefruit" and weekday in week_days:
    fruit_price = 1.45
elif fruit == "grapefruit" and weekday in weekends:
    fruit_price = 1.60
elif fruit == "kiwi" and weekday in week_days:
    fruit_price = 2.70
elif fruit == "kiwi" and weekday in weekends:
    fruit_price = 3.00
elif fruit == "pineapple" and weekday in week_days:
    fruit_price = 5.50
elif fruit == "pineapple" and weekday in weekends:
    fruit_price = 5.60
elif fruit == "grapes" and weekday in week_days:
    fruit_price = 3.85
elif fruit == "grapes" and weekday in weekends:
    fruit_price = 4.20

if fruit_price:
    total_price = fruit_quantity * fruit_price
    print(f"{total_price :.2f}")

# Solution 2 -> define a dictionary with prices,
# each of which is nested dictionary with product & price as kvp
