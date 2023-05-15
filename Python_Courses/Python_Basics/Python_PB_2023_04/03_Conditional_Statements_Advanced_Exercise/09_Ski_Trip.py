vacation_days = int(input())
vacation_type = input()
vacation_evaluation = input()

vacation_nights = vacation_days - 1
price_per_night = 0
if vacation_type == "room for one person":
    price_per_night = 18.00
elif vacation_type == "apartment":
    price_per_night = 25.00
    if vacation_nights < 10:
        price_per_night *= 0.70
    elif vacation_nights <= 15:
        price_per_night *= 0.65
    else:
        price_per_night *= 0.50
elif vacation_type == "president apartment":
    price_per_night = 35.00
    if vacation_nights < 10:
        price_per_night *= 0.90
    elif vacation_nights <= 15:
        price_per_night *= 0.85
    else:
        price_per_night *= 0.80

total_price = vacation_nights * price_per_night
if vacation_evaluation == "positive":
    total_price *= 1.25
elif vacation_evaluation == "negative":
    total_price *= 0.90

print(f"{total_price :.2f}")
