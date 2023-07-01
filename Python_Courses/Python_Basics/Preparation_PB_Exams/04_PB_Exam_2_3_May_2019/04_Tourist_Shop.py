budget = float(input())

budget_left = budget
counter = 0
command = input()
while command != "Stop":
    product = command
    counter += 1
    product_price = float(input())
    if counter % 3 == 0:
        product_price /= 2

    budget_left -= product_price
    if budget_left < 0:
        break

    command = input()

if command == "Stop":
    print(f"You bought {counter} products for {budget - budget_left :.2f} leva.")
else:
    print("You don't have enough money!")
    print(f"You need {-budget_left :.2f} leva!")
