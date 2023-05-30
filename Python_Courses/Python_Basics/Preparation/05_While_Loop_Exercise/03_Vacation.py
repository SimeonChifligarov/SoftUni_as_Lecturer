CONSECUTIVE_SPENDING_THRESHOLD = 5

total_days = 0
consecutive_spending = 0
is_failed = False

vacation_cost = float(input())
starting_money = float(input())

total_money = starting_money
while True:
    action = input()  # "spend" или "save"
    action_money = float(input())

    total_days += 1
    if action == "spend":
        consecutive_spending += 1
        if consecutive_spending >= CONSECUTIVE_SPENDING_THRESHOLD:
            is_failed = True
            break

        total_money -= action_money
        if total_money <= 0:
            total_money = 0

    elif action == "save":
        consecutive_spending = 0
        total_money += action_money

        if total_money >= vacation_cost:
            break


if not is_failed:
    print(f"You saved the money for {total_days} days.")
else:
    print("You can't save the money.")
    print(total_days)
