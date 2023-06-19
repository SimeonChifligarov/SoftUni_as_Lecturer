budget = float(input())
season = input()  # "Summer" or "Winter"

stay_type = ""
stay_location = ""
stay_price = 0
if budget <= 1000:
    stay_type = "Camp"
    if season == "Summer":
        stay_location = "Alaska"
        stay_price = 0.65 * budget
    elif season == "Winter":  # else:
        stay_location = "Morocco"
        stay_price = 0.45 * budget
elif budget <= 3000:
    stay_type = "Hut"
    if season == "Summer":
        stay_location = "Alaska"
        stay_price = 0.80 * budget
    elif season == "Winter":  # else:
        stay_location = "Morocco"
        stay_price = 0.60 * budget
elif budget > 3000:  # else:
    stay_type = "Hotel"
    if season == "Summer":
        stay_location = "Alaska"
        stay_price = 0.90 * budget
    elif season == "Winter":  # else:
        stay_location = "Morocco"
        stay_price = 0.90 * budget

print(f"{stay_location} - {stay_type} - {stay_price :.2f}")
