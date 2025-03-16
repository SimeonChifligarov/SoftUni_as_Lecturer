days = int(input())
room_type = input()  # "room for one person", "apartment", or "president apartment"
evaluation = input()  # "positive" or "negative"

price_per_night = 0.0
discount = 0.0
if room_type == 'room for one person':
    price_per_night = 18.00
    # if days < 10:
    #     # discount = 0.0
    #     pass
    # elif days <= 15:  # [10; 15]
    #     pass
    # else:  # (15; +inf) == [16; +inf)
    #     pass

elif room_type == 'apartment':
    price_per_night = 25.00
    if days < 10:
        discount = 0.30
    elif days <= 15:  # [10; 15]
        discount = 0.35
    else:  # (15; +inf) == [16; +inf)
        discount = 0.50

elif room_type == 'president apartment':  # else:
    price_per_night = 35.00
    if days < 10:
        discount = 0.10
    elif days <= 15:  # [10; 15]
        discount = 0.15
    else:  # (15; +inf) == [16; +inf)
        discount = 0.20

nights = days - 1
total_price = nights * price_per_night * (1 - discount)

if evaluation == 'positive':
    total_price *= 1.25  # добавя 25% от нея
elif evaluation == 'negative':  # else:
    total_price *= 0.90  # приспада от цената 10%

print(f'{total_price:.2f}')
