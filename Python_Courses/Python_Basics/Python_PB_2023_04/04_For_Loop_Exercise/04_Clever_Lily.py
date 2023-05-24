age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

total_money = 0
# toy_count = 0
for birthday in range(1, age + 1):  # [1, 2, 3, ..., 9, 10]
    if birthday % 2 == 0:
        total_money += birthday * 10 / 2
        total_money -= 1
    else:
        total_money += toy_price  # toy_count += 1

# total_money += toy_count * toy_price
if total_money >= washing_machine_price:
    print(f"Yes! {total_money - washing_machine_price :.2f}")
else:
    print(f"No! {washing_machine_price - total_money :.2f}")
