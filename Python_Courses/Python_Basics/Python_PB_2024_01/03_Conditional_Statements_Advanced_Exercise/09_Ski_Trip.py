days = int(input())
stay_type = input()  # "room for one person", "apartment", or "president apartment"
evaluation = input()  # "positive" or "negative"

# nights = days - 1
cost_per_night = 0
discount = 0
if stay_type == 'room for one person':
    cost_per_night = 18.00
elif stay_type == 'apartment':
    cost_per_night = 25.00
    if days < 10:
        discount = 0.30
    elif days <= 15:  # [10;15]
        discount = 0.35
    else:
        discount = 0.50
elif stay_type == 'president apartment':
    cost_per_night = 35.00
    if days < 10:
        discount = 0.10
    elif days <= 15:  # [10;15]
        discount = 0.15
    else:
        discount = 0.20

total_cost = (days - 1) * cost_per_night * (1 - discount)

if evaluation == 'positive':
    total_cost *= 1.25  # total_cost = total_cost * (1 + 0.25)
elif evaluation == 'negative':
    total_cost *= 0.90  # total_cost = total_cost * (1 - 0.10)

print(f'{total_cost :.2f}')
