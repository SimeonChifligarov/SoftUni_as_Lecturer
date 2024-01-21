flower_type = input()  # "Roses", "Dahlias", "Tulips", "Narcissus", or "Gladiolus"
flower_count = int(input())
budget = int(input())

# total_cost = 0
price_per_flower = 0
discount = 0

if flower_type == 'Roses':
    price_per_flower = 5
    if flower_count > 80:
        discount = 0.10  # 10 / 100
elif flower_type == 'Dahlias':
    price_per_flower = 3.80
    if flower_count > 90:
        discount = 0.15
elif flower_type == 'Tulips':
    price_per_flower = 2.80
    if flower_count > 80:
        discount = 0.15
elif flower_type == 'Narcissus':
    price_per_flower = 3
    if flower_count < 120:
        discount = -0.15
elif flower_type == 'Gladiolus':  # eq. else:  -> SoftUni guarantee correct input
    price_per_flower = 2.50
    if flower_count < 80:
        discount = -0.20

total_cost = flower_count * price_per_flower * (1 - discount)

if budget >= total_cost:
    money_left = budget - total_cost
    print(f'Hey, you have a great garden with {flower_count} {flower_type} and {money_left :.2f} leva left.')
else:
    money_needed = total_cost - budget
    print(f'Not enough money, you need {money_needed :.2f} leva more.')
