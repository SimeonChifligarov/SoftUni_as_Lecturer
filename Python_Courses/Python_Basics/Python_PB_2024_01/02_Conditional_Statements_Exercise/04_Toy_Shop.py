trip_cost = float(input())
puzzles_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

total_revenue = puzzles_count * 2.60 \
                + talking_dolls_count * 3 \
                + teddy_bears_count * 4.10 \
                + minions_count * 8.20 \
                + trucks_count * 2

# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена.
toys_total_count = puzzles_count + talking_dolls_count + teddy_bears_count + minions_count + trucks_count
discount = 0
if toys_total_count >= 50:
    discount = 0.25

total_revenue_after_discount = total_revenue * (1 - discount)

# От спечелените пари Петя трябва да даде 10% за наема на магазина.
# rent_money = total_revenue_after_discount * 0.10
# total_profit = total_revenue_after_discount - rent_money
total_profit = total_revenue_after_discount * (1 - 0.10)

if total_profit >= trip_cost:  # 1000 1000
    money_left = total_profit - trip_cost
    print(f'Yes! {money_left :.2f} lv left.')
else:
    money_needed = trip_cost - total_profit
    print(f'Not enough money! {money_needed :.2f} lv needed.')
