# TODO: refactor this one, using pay_per_km nested dictionary

MONTHS_IN_A_SEASON = 4
TAX_PERCENT = 10 / 100

season = input()  # "Spring", "Summer", "Autumn", or "Winter"
km = float(input())

pay_per_km = 0
if km <= 5_000:
    if season in ["Spring", "Autumn"]:
        pay_per_km = 0.75
    elif season == "Summer":  # elif season in ["Autumn"]
        pay_per_km = 0.90
    elif season == "Winter":
        pay_per_km = 1.05
elif km <= 10_000:
    if season in ["Spring", "Autumn"]:
        pay_per_km = 0.95
    elif season == "Summer":
        pay_per_km = 1.10
    elif season == "Winter":
        pay_per_km = 1.25
else:  # elif km > 10_000:
    if season in ["Spring", "Autumn"]:
        pay_per_km = 1.45
    elif season == "Summer":
        pay_per_km = 1.45
    elif season == "Winter":
        pay_per_km = 1.45

total_income = km * pay_per_km * MONTHS_IN_A_SEASON
net_income = total_income * (1 - TAX_PERCENT)

print(f"{net_income :.2f}")
