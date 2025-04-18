days = int(input())
stay_type = input()
evaluation = input()

night = days - 1
night_price = 0.0
discount = 0.0
if stay_type == 'room for one person':
    night_price = 18.00
    if days < 10:
        discount = 0.0
    elif days <= 15:
        discount = 0.0
    else:
        discount = 0.0
elif stay_type == 'apartment':
    night_price = 25.00
    if days < 10:
        discount = 0.30
    elif days <= 15:
        discount = 0.35
    else:
        discount = 0.50
elif stay_type == "president apartment":
    night_price = 35.00
    if days < 10:
        discount = 0.10
    elif days <= 15:
        discount = 0.15
    else:
        discount = 0.20

total_price = night * night_price * (1 - discount)

if evaluation == "positive":
    total_price *= 1.25
elif evaluation == "negative":
    total_price *= 0.90

print(f"{total_price:.2f}")
