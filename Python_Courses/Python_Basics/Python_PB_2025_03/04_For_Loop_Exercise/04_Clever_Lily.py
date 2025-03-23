toy_count = 0
total_gift_money = 0
gift_money = 0

age = int(input())
washing_machine_cost = float(input())
toy_price = int(input())

for bd in range(1, age + 1):  # 33 -> [1, 2, 3, 4 ... 33]
    if bd % 2 == 0:
        gift_money += 10  # 2 -> 10; 4 -> 10+10 == 20; 6 -> 20+10 == 30
        total_gift_money += gift_money
        total_gift_money -= 1  # for brother
    else:
        toy_count += 1
    # if bd % 2 != 0:
    #     toy_count += 1
    # else:
    #     gift_money += 10  # 2 -> 10; 4 -> 10+10 == 20; 6 -> 20+10 == 30
    #     total_money += gift_money
    #     total_money -= 1  # for brother

toy_money = toy_count * toy_price
total_money = total_gift_money + toy_money

is_goal_achieved = total_money >= washing_machine_cost

if is_goal_achieved:
    money_left = total_money - washing_machine_cost
    print(f'Yes! {money_left:.2f}')
else:
    money_needed = washing_machine_cost - total_money
    print(f'No! {money_needed:.2f}')

