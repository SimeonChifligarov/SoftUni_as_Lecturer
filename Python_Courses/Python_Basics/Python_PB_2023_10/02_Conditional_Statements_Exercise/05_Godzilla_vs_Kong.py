budget = float(input())
extras = int(input())
clothing_for_extra = float(input())

decor = budget * 0.10
if extras > 150:
    clothing_for_extra = clothing_for_extra * 0.90

money_needed = decor + extras * clothing_for_extra

if budget >= money_needed:
    print(f"Action!\nWingard starts filming with {budget - money_needed :.2f} leva left.")
else:
    print(f"Not enough money!\nWingard needs {money_needed - budget :.2f} leva more.")
