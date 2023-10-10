vacation_cost = float(input())
puzzles_count = int(input())
talking_dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

money_earned = puzzles_count * 2.60 \
               + talking_dolls_count * 3 \
               + teddy_bears_count * 4.10 \
               + minions_count * 8.20 \
               + trucks_count * 2

total_count = puzzles_count + talking_dolls_count + teddy_bears_count + minions_count + trucks_count
# discount_percent = ...
if total_count >= 50:
    money_earned = money_earned * (1 - 0.25)  # money_earned *= (1 - 0.25)

# rent_cost = 0.10 * money_earned
# money_earned -= rent_cost
money_earned = money_earned * (1 - 0.1)

if money_earned >= vacation_cost:  # 1300 >= 1000
    # money_left = money_earned - vacation_cost
    print(f"Yes! {money_earned - vacation_cost :.2f} lv left.")
else:
    # money_not_enough = vacation_cost - money_earned
    print(f"Not enough money! {vacation_cost - money_earned :.2f} lv needed.")
