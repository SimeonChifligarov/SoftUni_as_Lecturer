budget = int(input())
season = input()  # "Spring", "Summer", "Autumn", or "Winter"
fishermen = int(input())

boat_cost = 0
if season == 'Spring':
    boat_cost = 3000
elif season == 'Summer' or season == 'Autumn':
    boat_cost = 4200
elif season == 'Winter':  # eq. else:
    boat_cost = 2600

discount = 0
if fishermen <= 6:
    discount = 0.10
elif fishermen <= 11:  # fishermen is in range [7; 11]
    discount = 0.15
else:  # eq. elif fishermen >= 12:
    discount = 0.25

# Рибарите ползват допълнително 5% отстъпка, ако са четен брой, освен ако не е есен
extra_discount = 0
if fishermen % 2 == 0 and season != 'Autumn':
    extra_discount = 0.05  # discount = discount + 0.05

total_cost = boat_cost * (1 - discount) * (1 - extra_discount)

if budget >= total_cost:
    money_left = budget - total_cost
    print(f'Yes! You have {money_left :.2f} leva left.')
else:
    money_need = total_cost - budget
    print(f'Not enough money! You need {money_need :.2f} leva.')
