age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

total_money = 0
total_toys = 0
for bd in range(1, age + 1):  # birthday
    # print(bd)
    if bd % 2 == 0:
        total_money += bd * 5
        total_money -= 1  # brother takes 1
    else:
        total_toys += 1

# Lilly is selling her toys to get money for the washing machine
total_toys_money = total_toys * toy_price
final_money = total_money + total_toys_money

if final_money >= washing_machine_price:  # abs(  )
    diff = final_money - washing_machine_price
    print(f'Yes! {diff :.2f}')
else:
    diff = washing_machine_price - final_money
    print(f'No! {diff :.2f}')
