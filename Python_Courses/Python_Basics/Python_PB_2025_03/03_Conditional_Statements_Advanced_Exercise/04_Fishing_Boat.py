budget = int(input())
season = input()  # "Spring", "Summer", "Autumn", or "Winter"
fishermen = int(input())

rent_cost = 0
if season == 'Spring':
    rent_cost = 3000
# elif season == 'Summer' or season == 'Autumn':
elif season in ('Summer', 'Autumn'):
    rent_cost = 4200
elif season == 'Winter':
    rent_cost = 2600

discount = 0.0
if fishermen <= 6:
    discount = 0.10  # Ако групата е до 6 човека включително  -  отстъпка от 10%;
elif fishermen <= 11:  # (6; 11]  ; [7; 11]
    discount = 0.15  # Ако групата е от 7 до 11 човека включително  -  отстъпка от 15%;
else:
    discount = 0.25  # Ако групата е от 12 нагоре  -  отстъпка от 25%.

extra_discount = 0.0
if fishermen % 2 == 0 and season != 'Autumn':  # ако са четен брой И не е есен
    extra_discount = 0.05  # 5%  # допълнително 5% отстъпка

total_cost = rent_cost * (1 - discount) * (1 - extra_discount)

is_budget_enough = budget >= total_cost  # True/False

if is_budget_enough:
    money_left = budget - total_cost
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    money_needed = total_cost - budget
    print(f'Not enough money! You need {money_needed:.2f} leva.')
