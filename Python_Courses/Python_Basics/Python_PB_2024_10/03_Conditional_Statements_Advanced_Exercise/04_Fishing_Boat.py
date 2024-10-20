budget = int(input())
season = input()  # "Spring", "Summer", "Autumn", or "Winter"
fishermen = int(input())

boat_price = 0
if season == 'Spring':
    boat_price = 3000
elif season == 'Summer' or season == 'Autumn':
    boat_price = 4200
elif season == 'Winter':
    boat_price = 2600

discount = 0.0
if fishermen <= 6:  # (-inf, 6]
    discount = 0.10
# elif 7 <= fishermen <= 11:
elif fishermen <= 11:  # (6, 11]  == [7, 11]
    discount = 0.15
# elif fishermen >= 12:
else:  # [12, inf)
    discount = 0.25

extra_discount = 0.0
if fishermen % 2 == 0 and season != 'Autumn':
    extra_discount = 0.05

total_price = boat_price * (1 - discount) * (1 - extra_discount)

if budget >= total_price:
    money_left = budget - total_price
    print(f'Yes! You have {money_left :.2f} leva left.')
else:
    money_needed = total_price - budget
    print(f'Not enough money! You need {money_needed :.2f} leva.')
