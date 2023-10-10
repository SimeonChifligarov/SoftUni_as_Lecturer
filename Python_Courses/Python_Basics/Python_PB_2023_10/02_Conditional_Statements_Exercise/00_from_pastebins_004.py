# •   Пъзел - 2.60 лв.
# •   Говореща кукла - 3 лв.
# •   Плюшено мече - 4.10 лв.
# •   Миньон - 8.20 лв.
# •   Камионче - 2 лв.
#
# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена
#
# От спечелените пари Петя трябва да даде 10% за наема на магазина.
#
# 1.    Цена на екскурзията - реално число в интервала [1.00 … 10000.00]
# 2.    Брой пъзели - цяло число в интервала [0… 1000]
# 3.    Брой говорещи кукли - цяло число в интервала [0 … 1000]
# 4.    Брой плюшени мечета - цяло число в интервала [0 … 1000]
# 5.    Брой миньони - цяло число в интервала [0 … 1000]
# 6.    Брой камиончета - цяло число в интервала [0 … 1000]

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
    + trucks_count * 2.00

# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена

total_count = puzzles_count + talking_dolls_count + teddy_bears_count + minions_count + trucks_count
if total_count >= 50:
    money_earned = money_earned * (1 - 0.25)  # = money_earned *= (1 - 0.25)

# От спечелените пари Петя трябва да даде 10% за наема на магазина.
money_earned = money_earned * (1 - 0.1)

if money_earned >= vacation_cost:  # 1300 >= 1000
    print(f"Yes! {money_earned - vacation_cost :.2f} lv left.")
else:
    print(f"Not enough money! {vacation_cost - money_earned :.2f} lv needed.")
# •   Ако парите са достатъчни се отпечатва:
# o "Yes! {оставащите пари} lv left."
# •   Ако парите НЕ са достатъчни се отпечатва:
# o "Not enough money! {недостигащите пари} lv needed."