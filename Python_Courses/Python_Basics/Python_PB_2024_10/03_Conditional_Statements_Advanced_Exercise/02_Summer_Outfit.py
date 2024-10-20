degrees = int(input())
daytime = input()  # "Morning", "Afternoon", "Evening"

outfit = ''
shoes = ''
# 10 <= градуси <= 18
# 18 < градуси <= 24
# градуси >= 25

if daytime == 'Morning':
    if 10 <= degrees <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < degrees <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degrees >= 25:
        outfit = 'T-Shirt'
        shoes = 'Sandals'

elif daytime == 'Afternoon':
    if 10 <= degrees <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degrees <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif degrees >= 25:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'

elif daytime == 'Evening':
    # outfit = 'Shirt'
    # shoes = 'Moccasins'
    if 10 <= degrees <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degrees <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degrees >= 25:
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f'It\'s {degrees} degrees, get your {outfit} and {shoes}.')
