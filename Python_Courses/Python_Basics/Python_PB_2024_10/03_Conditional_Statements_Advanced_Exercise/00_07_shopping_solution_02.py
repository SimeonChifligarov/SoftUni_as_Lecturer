# 07_Shopping

# 1.    Бюджетът на Петър - реално число в интервала [1.0…100000.0]
budget = float(input())
# 2.    Броят видеокарти - цяло число в интервала [1…100]
gpu_count = int(input())
# 3.    Броят процесори - цяло число в интервала [1…100]
cpu_count = int(input())
# 4.    Броят рам памет - цяло число в интервала [1…100]
ram_count = int(input())

# •   Видеокарта – 250 лв./бр.
gpu_price = 250

total_gpu_cost = gpu_count * gpu_price

# •   Процесор – 35% от цената на закупените видеокарти/бр.
cpu_price = total_gpu_cost * 0.35
# •   Рам памет – 10% от цената на закупените видеокарти/бр.
ram_price = total_gpu_cost * 0.10

total_cpu_cost = cpu_count * cpu_price
total_ram_cost = ram_count * ram_price

total_cost = total_gpu_cost + total_cpu_cost + total_ram_cost

# Ако броя на видеокартите е по-голям от този на процесорите получава 15% отстъпка от крайната сметка

if gpu_count > cpu_count:
    total_cost *= 0.85

if budget >= total_cost:
    money_left = budget - total_cost
    print(f'You have {money_left :.2f} leva left!')

else:
    money_needed = total_cost - budget
    print(f'Not enough money! You need {money_needed :.2f} leva more!')
