budget = int(input())
seasons = input()
fishers = int(input())

ship = 0
# · Цената за наем на кораба през пролетта е 3000 лв.;
# · Цената за наем на кораба през лятото и есента е 4200 лв.;
# · Цената за наем на кораба през лятото и есента е 4200 лв.;
# · Цената за наем на кораба през зимата е 2600 лв.

total = 0
discount = 0
if seasons == 'Spring':
    ship = 3000
    # · Ако групата е до 6 човека включително - отстъпка от 10%;
    if fishers <= 6:
        discount = 0.1
    # · Ако групата е от 7 до 11 човека включително - отстъпка от 15%;
    elif 7 <= fishers <= 11:
        discount = 0.15
    # · Ако групата е от 12 нагоре - отстъпка от 25%.
    else:
        discount = 0.25
elif seasons == 'Summer' or seasons == 'Autumn':
    ship = 4200
    # · Ако групата е до 6 човека включително - отстъпка от 10%;
    if fishers <= 6:
        discount = 0.1
    # · Ако групата е от 7 до 11 човека включително - отстъпка от 15%;
    elif 7 <= fishers <= 11:
        discount = 0.15
    # · Ако групата е от 12 нагоре - отстъпка от 25%.
    elif fishers >= 12:
        discount = 0.25
elif seasons == 'Winter':
    ship = 2600
    # · Ако групата е до 6 човека включително - отстъпка от 10%;
    if fishers <= 6:
        discount = 0.1
    # · Ако групата е от 7 до 11 човека включително - отстъпка от 15%;
    elif 7 <= fishers <= 11:
        discount = 0.15
    # · Ако групата е от 12 нагоре - отстъпка от 25%.
    elif fishers >= 12:
        discount = 0.25

# 5 % отстъпка, ако са четен брой, освен ако не е есен
extra_discount = 0
if fishers % 2 == 0 and seasons != 'Autumn':
    extra_discount += 0.05

total = ship * (1 - discount) * (1 - extra_discount)

if total <= budget:
    money_left = budget - total
    print(f'Yes! You have {money_left:.2f} leva left.')
else:
    money_nedeed = total - budget
    print(f'Not enough money! You need {money_nedeed:.2f} leva.')
