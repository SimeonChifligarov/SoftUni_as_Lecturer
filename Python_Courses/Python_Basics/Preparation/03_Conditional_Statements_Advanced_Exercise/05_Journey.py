budget = float(input())
season = input()  # "summer” или "winter”

vacation_type = ""
vacation_destination = ""
vacation_price = 0
if budget <= 100:
    vacation_destination = "Bulgaria"
    if season == "summer":
        vacation_type = "Camp"
        vacation_price = budget * 0.30
    elif season == "winter":
        vacation_type = "Hotel"
        vacation_price = budget * 0.70
elif budget <= 1000:
    vacation_destination = "Balkans"
    if season == "summer":
        vacation_type = "Camp"
        vacation_price = budget * 0.40
    elif season == "winter":
        vacation_type = "Hotel"
        vacation_price = budget * 0.80
elif budget > 1000:
    vacation_destination = "Europe"
    vacation_type = "Hotel"
    vacation_price = budget * 0.90

print(f"Somewhere in {vacation_destination}")
print(f"{vacation_type} - {vacation_price :.2f}")
