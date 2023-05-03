RENT_AS_MULTIPLIER = 0.1

PUZZLE_PRICE = 2.60
TALKING_DOLL_PRICE = 3.00
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2.00

vacation_price = float(input())
puzzle_count = int(input())
talking_doll_count = int(input())
teddy_bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена.
# От спечелените пари Петя трябва да даде 10% за наема на магазина.
# Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.

total_count = puzzle_count + talking_doll_count + teddy_bear_count + minion_count + truck_count

discount = 0
if total_count >= 50:
    discount = 0.25

total_price = puzzle_count * PUZZLE_PRICE + talking_doll_count * TALKING_DOLL_PRICE \
              + teddy_bear_count * TEDDY_BEAR_PRICE + minion_count * MINION_PRICE \
              + truck_count * TRUCK_PRICE

total_price_with_discount = total_price * (1 - discount)
total_money = total_price_with_discount * (1 - RENT_AS_MULTIPLIER)

if total_money >= vacation_price:
    print(f"Yes! {total_money - vacation_price :.2f} lv left.")
else:
    print(f"Not enough money! {vacation_price - total_money :.2f} lv needed.")
