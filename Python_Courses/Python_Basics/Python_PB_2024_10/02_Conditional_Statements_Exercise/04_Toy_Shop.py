vacation_cost = float(input())
puzzles_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

income = (puzzles_count * 2.60 +
          talking_dolls_count * 3 +
          teddy_bears_count * 4.10 +
          minions_count * 8.20 +
          trucks_count * 2)

total_count = puzzles_count + talking_dolls_count + teddy_bears_count + minions_count + trucks_count

discount = 0
if total_count >= 50:
    # income = income * 0.75  # income *= 0.75
    discount = 0.25  # 25% == 25 / 100 == 0.25

total_income = income * (1 - discount)  # income * (1 - 0.25) == income * 0.75

# От спечелените пари Петя трябва да даде 10% за наема на магазина.
final_income = total_income * 0.90

if final_income >= vacation_cost:
    money_left = final_income - vacation_cost
    print(f'Yes! {money_left :.2f} lv left.')
else:
    money_needed = vacation_cost - final_income
    print(f'Not enough money! {money_needed :.2f} lv needed.')
