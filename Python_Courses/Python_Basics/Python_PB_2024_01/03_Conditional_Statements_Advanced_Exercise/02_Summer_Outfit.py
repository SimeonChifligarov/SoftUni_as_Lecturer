degrees = int(input())
daytime = input()  # "Morning", "Afternoon", or "Evening".

# Outfit = Sweatshirt
# Shoes = Sneakers

outfit = ''
shoes = ''


if daytime == 'Morning':
    if 10 <= degrees <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < degrees <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    # elif degrees >= 25:
    else:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
elif daytime == 'Afternoon':
    if 10 <= degrees <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degrees <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
        # elif degrees >= 25:
    else:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
elif daytime == 'Evening':
    if 10 <= degrees <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degrees <= 24:
        outfit = 'T-Shirt'
        shoes = 'Moccasins'
    # elif degrees >= 25:
    else:
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f'It\'s {degrees} degrees, get your {outfit} and {shoes}.')
