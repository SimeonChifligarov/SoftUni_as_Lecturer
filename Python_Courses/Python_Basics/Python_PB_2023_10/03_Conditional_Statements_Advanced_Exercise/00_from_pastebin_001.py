flower_type = input()
flower_count = int(input())
budget = int(input())

total_cost = 0
flower_price = 0
Discount = 0  # snake_case
if flower_type == "Roses":
    flower_price = 5
    if flower_count > 80:
        Discount = 0.10
elif flower_type == "Tulips":
    flower_price = 2.80
    if flower_count > 80:
        Discount = 0.15
elif flower_type == "Dahlias":
    flower_price = 3.80
    if flower_count > 90:
        Discount = 0.15
elif flower_type == "Narcissus":
    flower_price = 3
    if flower_count < 120:
        Discount = -0.15
elif flower_type == "Gladiolus":
    flower_price = 2.50
    if flower_count < 80:
        Discount = - 0.20

total_cost = flower_count * flower_price * (1 - Discount)  # True; False

if budget >= total_cost:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {budget - total_cost:.2f} leva left.")
else:
    print(f"Not enough money, you need {total_cost - budget:.2f} leva more.")
