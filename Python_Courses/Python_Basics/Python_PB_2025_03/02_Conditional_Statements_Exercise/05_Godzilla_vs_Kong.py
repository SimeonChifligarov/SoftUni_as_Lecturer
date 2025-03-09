# Ред 1.	Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
budget = float(input())
# Ред 2.	Брой на статистите – цяло число в интервала [1 … 500]
walk_on_count = int(input())
# Ред 3.	Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]
costume_price = float(input())

# •	Декорът за филма е на стойност 10% от бюджета.
decor_cost = budget * 0.10

# •	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.
if walk_on_count > 150:
    costume_price *= 0.90  # clothes_price = clothes_price * (1 - 0.1)

walk_on_cost = walk_on_count * costume_price

total_cost = decor_cost + walk_on_cost

if budget >= total_cost:  # if decor + walk_on_count * clothes_price <= budget:
    print('Action!')
    print(f'Wingard starts filming with {abs(budget - total_cost):.2f} leva left.')
else:
    print('Not enough money!')
    print(f'Wingard needs {abs(budget - total_cost):.2f} leva more.')
