# •	Градусите - цяло число;
# •	Време от денонощието - текст с три възможности "Morning", "Afternoon" или "Evening".

degrees = int(input())
daytime = input()  # "Morning", "Afternoon", "Evening"

outfit = ''
shoes = ''

if daytime == 'Morning':  # if 10 <= degrees <= 18:
    if 10 <= degrees <= 18:  #       if daytime == 'Morning':... elif daytime == 'Afternoon':... elif daytime == '':...
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < degrees <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degrees >= 25:  # else:
        outfit = 'T-Shirt'
        shoes = 'Sandals'

elif daytime == 'Afternoon':
    if 10 <= degrees <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degrees <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif degrees >= 25:  # else:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'

elif daytime == 'Evening':  # else:
    if 10 <= degrees <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < degrees <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif degrees >= 25:  # else:
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f'It\'s {degrees} degrees, get your {outfit} and {shoes}.')
