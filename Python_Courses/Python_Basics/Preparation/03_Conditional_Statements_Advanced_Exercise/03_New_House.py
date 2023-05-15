ROSE_PRICE = 5.00
DAHLIA_PRICE = 3.80
TULIP_PRICE = 2.80
NARCISSUS_PRICE = 3.00
GLADIOLUS_PRICE = 2.50

flower_type = input()
flower_count = int(input())
budget = int(input())

price = 0
discount = 0
if flower_type == "Roses":
    price = ROSE_PRICE
    if flower_count > 80:
        discount = 0.10
elif flower_type == "Dahlias":
    price = DAHLIA_PRICE
    if flower_count > 90:
        discount = 0.15
elif flower_type == "Tulips":
    price = TULIP_PRICE
    if flower_count > 80:
        discount = 0.15
elif flower_type == "Narcissus":
    price = NARCISSUS_PRICE
    if flower_count < 120:
        discount = -0.15
elif flower_type == "Gladiolus":
    price = GLADIOLUS_PRICE
    if flower_count < 80:
        discount = -0.20

total_price = flower_count * price * (1 - discount)

if budget >= total_price:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} "
          f"and {budget - total_price :.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budget :.2f} leva more.")
