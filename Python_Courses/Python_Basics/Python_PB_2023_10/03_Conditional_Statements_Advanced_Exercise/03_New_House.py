flower_type = input()  # "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus"
flower_count = int(input())
budget = int(input())

flower_price = 0
discount = 0

if flower_type == "Roses":
    flower_price = 5
    if flower_count > 80:
        discount = 0.10
elif flower_type == "Dahlias":
    flower_price = 3.80
    if flower_count > 90:
        discount = 0.15
elif flower_type == "Tulips":
    flower_price = 2.80
    if flower_count > 80:
        discount = 0.15
elif flower_type == "Narcissus":
    flower_price = 3
    if flower_count < 120:
        discount = -0.15
elif flower_type == "Gladiolus":  # eq "else:" IF valid input is guaranteed
    flower_price = 2.50
    if flower_count < 80:
        discount = -0.20

total_cost = flower_count * flower_price * (1 - discount)

if budget >= total_cost:  # 1000; 1000
    money_extra = budget - total_cost
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {money_extra :.2f} leva left.")
else:
    money_not_enough = total_cost - budget
    print(f"Not enough money, you need {money_not_enough :.2f} leva more.")
