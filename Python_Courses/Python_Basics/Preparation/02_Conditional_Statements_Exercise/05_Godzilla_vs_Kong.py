budget = float(input())
walk_on_count = int(input())
clothes_price_per_walk_on = float(input())

decor = budget * 0.10
if walk_on_count > 150:
    clothes_price_per_walk_on *= 0.90

money_needed = decor + walk_on_count * clothes_price_per_walk_on

MESSAGE_FOR_BUDGET_ENOUGH = f"Action!\nWingard starts filming with {budget - money_needed :.2f} leva left."
MESSAGE_FOR_BUDGET_NOT_ENOUGH = f"Not enough money!\nWingard needs {money_needed - budget :.2f} leva more."

if money_needed > budget:
    print(MESSAGE_FOR_BUDGET_NOT_ENOUGH)
else:
    print(MESSAGE_FOR_BUDGET_ENOUGH)
