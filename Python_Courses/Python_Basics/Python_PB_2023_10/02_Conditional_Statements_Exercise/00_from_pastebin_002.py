jigsaw = 2.60
talking_doll = 3.00
teddy_bear = 4.10
mignon = 8.20
truck = 2.00

cost_of_excursion = float(input())
number_of_jigsaw = int(input())
number_of_talking_doll = int(input())
number_of_teddy_bear = int(input())
number_of_mignon = int(input())
number_of_truck = int(input())
price = 0
jigsaw_price = number_of_jigsaw * jigsaw
talking_doll_price = number_of_talking_doll * talking_doll
teddy_bear_price = number_of_teddy_bear * teddy_bear
mignon_price = number_of_mignon * mignon
truck_price = number_of_truck * truck
total_price = jigsaw_price + talking_doll_price + teddy_bear_price + mignon_price + truck_price
rest_money = 0
toys = number_of_jigsaw + number_of_talking_doll + number_of_teddy_bear + number_of_mignon + number_of_truck
discount = total_price * 0.25
if toys >= 50:
    total_price = (total_price - discount)

total_price = total_price * (1 - 0.10)
if total_price >= cost_of_excursion:
    rest_money = total_price - cost_of_excursion
    print(f"Yes!{rest_money: .2f} lv left.")
else:
    rest_money = cost_of_excursion - total_price
    print(f"Not enough money!{rest_money: .2f} lv needed.")
