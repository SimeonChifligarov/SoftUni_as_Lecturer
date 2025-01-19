days = int(input())
vacation_type = input()  # "room for one person", "apartment", or "president apartment"
mood = input()  # "positive" or "negative"

nights = days - 1

price_per_night = 0.0
discount = 0.0
if vacation_type == 'room for one person':
    price_per_night = 18.00
    if nights < 10:
        discount = 0.0  # pass
    elif nights <= 15:  # [10; 15]
        discount = 0.0
    elif nights > 15:  # else:
        discount = 0.0

elif vacation_type == 'apartment':
    price_per_night = 25.00
    if nights < 10:
        discount = 0.30  # pass
    elif nights <= 15:  # [10; 15]
        discount = 0.35
    elif nights > 15:  # else:
        discount = 0.50

elif vacation_type == 'president apartment':  # else:
    price_per_night = 35.00
    if nights < 10:
        discount = 0.10  # pass
    elif nights <= 15:  # [10; 15]
        discount = 0.15
    elif nights > 15:  # else:
        discount = 0.20

total_price = price_per_night * nights
total_price_after_discount = total_price * (1 - discount)

if mood == 'positive':
    total_price_after_discount *= 1.25  # total_price_after_discount = total_price_after_discount * 1.25
elif mood == 'negative':
    total_price_after_discount *= 0.90

print(f'{total_price_after_discount:.2f}')
