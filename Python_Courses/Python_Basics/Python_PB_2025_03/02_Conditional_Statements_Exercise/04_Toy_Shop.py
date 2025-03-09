# •	Пъзел - 2.60 лв.
# •	Говореща кукла - 3 лв.
# •	Плюшено мече - 4.10 лв.
# •	Миньон - 8.20 лв.
# •	Камионче - 2 лв.

# 1. E
vacation_cost = float(input())
puzzles_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
car_toys_count = int(input())

# 2. T

total_income = (
    puzzles_count * 2.60
    + talking_dolls_count * 3.00
    + teddy_bears_count * 4.10
    + minions_count * 8.20
    + car_toys_count * 2.00
)

# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена
total_toys = puzzles_count + talking_dolls_count + teddy_bears_count + minions_count + car_toys_count
discount = 0.0
if total_toys >= 50:
    discount = 0.25  # 25 per cent = 25 / 100 == 0.25

total_income_after_discount = total_income * (1 - discount)  # total_income * (1 - 0.25) = total_income * 0.75

# От спечелените пари Петя трябва да даде 10% за наема на магазина.
rent_cost = total_income_after_discount * 0.10

final_income = total_income_after_discount - rent_cost

# 3. L
if final_income >= vacation_cost:
    money_left = final_income - vacation_cost
    print(f'Yes! {money_left:.2f} lv left.')
else:
    money_needed = vacation_cost - final_income
    print(f'Not enough money! {money_needed:.2f} lv needed.')
