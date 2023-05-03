PUZZLE_PRICE = 2.60
TALKING_DOLL_PRICE = 3.00
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2.00

vacation_cost = float(input())
puzzle_count = int(input())
talking_doll_count = int(input())
teddy_bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

total_count = puzzle_count + talking_doll_count + teddy_bear_count + minion_count + truck_count

discount = 0
if total_count >= 50:
    discount = 0.25

total_income = puzzle_count * PUZZLE_PRICE \
               + talking_doll_count * TALKING_DOLL_PRICE \
               + teddy_bear_count * TEDDY_BEAR_PRICE \
               + minion_count * MINION_PRICE \
               + truck_count * TRUCK_PRICE

total_income_with_discount = total_income * (1 - discount)

rent_cost = total_income_with_discount * 0.10

final_income = total_income_with_discount - rent_cost

if final_income >= vacation_cost:
    print(f"Yes! {final_income - vacation_cost :.2f} lv left.")
else:
    print(f"Not enough money! {vacation_cost - final_income :.2f} lv needed.")
