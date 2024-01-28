age = int(input())
washing_machine = float(input())
toy_price = int(input())

toys_count = 0
budget = 0

for birthday in range(1, age + 1):  # [1, 2, 3, ... age]
    if birthday % 2 == 0:
        birthday_money = birthday * 5  # 2 -> 10, 4 -> 20, 6 -> 30
        budget += birthday_money
        budget -= 1
    else:
        toys_count += 1

budget += toy_price * toys_count

if budget >= washing_machine:
    diff = budget - washing_machine
    print(f'Yes! {diff :.2f}')
else:
    diff = washing_machine - budget
    print(f'No! {diff :.2f}')
