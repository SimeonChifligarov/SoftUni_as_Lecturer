# цвете             	Роза	Далия	Лале	Нарцис	Гладиола
# Цена на брой в лева	5	   3.80  	2.80	3	    2.50

flower_type = input()  # "Roses", "Dahlias", "Tulips", "Narcissus", or "Gladiolus"
flower_count = int(input())
budget = int(input())

flower_price = 0.0
discount = 0.0
if flower_type == 'Roses':
    flower_price = 5.00
    # •	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
    if flower_count > 80:
        discount = 0.10  # 10% == 10 per cent == 10 / 100 == 0.10

elif flower_type == 'Dahlias':
    flower_price = 3.80
    # •	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
    if flower_count > 90:
        discount = 0.15

elif flower_type == 'Tulips':
    flower_price = 2.80
    # •	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
    if flower_count > 80:
        discount = 0.15
elif flower_type == 'Narcissus':
    flower_price = 3.00
    # •	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
    if flower_count < 120:
        discount = -0.15

elif flower_type == 'Gladiolus':  # else:
    flower_price = 2.50
    # •	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.
    if flower_count < 80:
        discount = -0.20

total_price = flower_count * flower_price * (1 - discount)

if budget >= total_price:
    money_left = budget - total_price
    print(f'Hey, you have a great garden with {flower_count} {flower_type} and {money_left:.2f} leva left.')
else:
    money_needed = total_price - budget
    print(f'Not enough money, you need {money_needed:.2f} leva more.')
