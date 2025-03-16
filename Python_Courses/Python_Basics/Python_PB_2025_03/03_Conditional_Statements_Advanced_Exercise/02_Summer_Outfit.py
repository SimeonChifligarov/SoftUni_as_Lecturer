degrees = int(input())
time_of_day = input()  # "Morning", "Afternoon", or "Evening"

outfit = ''
shoes = ''
if time_of_day == 'Morning':
    if 10 <= degrees <= 18:  # 10 <= градуси <= 18
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < degrees <= 24:  # 18 < градуси <= 24
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degrees >= 25:  # градуси >= 25
        outfit = 'T-Shirt'
        shoes = 'Sandals'

elif time_of_day == 'Afternoon':
    if 10 <= degrees <= 18:  # 10 <= градуси <= 18
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degrees <= 24:  # 18 < градуси <= 24
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif degrees >= 25:  # градуси >= 25
        outfit = 'Swim Suit'
        shoes = 'Barefoot'

elif time_of_day == 'Evening':  # else:
    if 10 <= degrees <= 18:  # 10 <= градуси <= 18
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degrees <= 24:  # 18 < градуси <= 24
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degrees >= 25:  # градуси >= 25
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f'It\'s {degrees} degrees, get your {outfit} and {shoes}.')
