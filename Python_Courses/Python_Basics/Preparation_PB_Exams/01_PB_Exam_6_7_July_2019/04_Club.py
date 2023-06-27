target_profit = float(input())
total_profit = 0

is_success = False
command = input()
while command != "Party!":
    cocktail = command
    count = int(input())

    cocktail_price = len(cocktail)

    total_price = cocktail_price * count
    if total_price % 2 != 0:
        total_price *= 0.75

    total_profit += total_price
    if total_profit >= target_profit:
        is_success = True
        break

    command = input()

if is_success:
    print("Target acquired.")
else:
    print(f"We need {target_profit - total_profit :.2f} leva more.")

print(f"Club income - {total_profit :.2f} leva.")
