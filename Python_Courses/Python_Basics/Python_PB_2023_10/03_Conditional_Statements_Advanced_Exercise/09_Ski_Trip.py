days = int(input())
type_stay = input()  # "room for one person", "apartment" или "president apartment"
evaluation = input()  # "positive"  или "negative"

nights = days - 1
cost_per_day = 0
discount = 0

if type_stay == "room for one person":
    cost_per_day = 18.00
    if days < 10:
        discount = 0
    elif days <= 15:  # [10; 15]
        discount = 0
    else:
        discount = 0
elif type_stay == "apartment":
    cost_per_day = 25.00
    if days < 10:
        discount = 0.30
    elif days <= 15:  # [10; 15]
        discount = 0.35
    else:
        discount = 0.50
elif type_stay == "president apartment":  # else:
    cost_per_day = 35.00
    if days < 10:
        discount = 0.10
    elif days <= 15:  # [10; 15]
        discount = 0.15
    else:
        discount = 0.20

total_cost = nights * cost_per_day * (1 - discount)  # (days - 1) * ...
if evaluation == "positive":
    total_cost *= 1.25
    # total_cost = total_cost * (1 + 0.25)
elif evaluation == "negative":
    total_cost *= 0.90

print(f"{total_cost :.2f}")
