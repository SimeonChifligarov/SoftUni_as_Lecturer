temperature = int(input())
day_time = input()
Outfit = ''
Shoes = ''
if 10 <= temperature <= 18:
    if day_time == 'Morning':
        Outfit = 'Sweatshirt'
        Shoes = 'Sneakers'
    elif day_time == 'Afternoon':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif day_time == 'Evening':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'

elif 18 < temperature <= 24:
    if day_time == 'Morning':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif day_time == 'Afternoon':
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
    elif day_time == 'Evening':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'

elif temperature >= 25:
    if day_time == 'Morning':
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
    elif day_time == 'Afternoon':
        Outfit = 'Swim Suit'
        Shoes = 'Barefoot'
    elif day_time == 'Evening':
        Outfit = 'Shirt'
        Shoes = 'Moccasins'

print(f"It's {temperature} degrees, get your {Outfit} and {Shoes}.")
