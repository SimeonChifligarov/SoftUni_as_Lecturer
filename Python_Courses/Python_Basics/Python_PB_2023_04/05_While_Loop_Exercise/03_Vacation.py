vacation_cost = float(input())
starting_money = float(input())

total_days = 0
consecutive_spend_days = 0

total_money = starting_money
are_money_enough = False
while True:
    action = input()  # "spend" или "save"
    current_amount = float(input())
    total_days += 1

    if action == "spend":
        consecutive_spend_days += 1
        total_money -= current_amount
        if total_money < 0:
            total_money = 0

        if consecutive_spend_days >= 5:
            break

    elif action == "save":
        consecutive_spend_days = 0
        total_money += current_amount
        if total_money >= vacation_cost:
            are_money_enough = True
            break


if are_money_enough:
    print(f"You saved the money for {total_days} days.")
else:
    print("You can't save the money.")
    print(total_days)
