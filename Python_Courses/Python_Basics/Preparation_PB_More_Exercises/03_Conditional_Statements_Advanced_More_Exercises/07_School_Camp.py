season = input()  # “Winter”, “Spring”, or “Summer”
group_type = input()  # “boys”, “girls”, or “mixed”
group_count = int(input())
nights_count = int(input())

price_per_night = 0
sport_type = ""
if group_type == "boys":
    if season == "Winter":
        price_per_night = 9.60
        sport_type = "Judo"
    elif season == "Spring":
        price_per_night = 7.20
        sport_type = "Tennis"
    elif season == "Summer":  # else:
        price_per_night = 15
        sport_type = "Football"
elif group_type == "girls":
    if season == "Winter":
        price_per_night = 9.60
        sport_type = "Gymnastics"
    elif season == "Spring":
        price_per_night = 7.20
        sport_type = "Athletics"
    elif season == "Summer":  # else:
        price_per_night = 15
        sport_type = "Volleyball"
elif group_type == "mixed":  # else:
    if season == "Winter":
        price_per_night = 10
        sport_type = "Ski"
    elif season == "Spring":
        price_per_night = 9.50
        sport_type = "Cycling"
    elif season == "Summer":  # else:
        price_per_night = 20
        sport_type = "Swimming"

discount = 0
if group_count >= 50:
    discount = 50 / 100
elif group_count >= 20:
    discount = 15 / 100
elif group_count >= 10:
    discount = 5 / 100

price_per_night *= (1 - discount)
total_price = price_per_night * nights_count * group_count

print(f"{sport_type} {total_price :.2f} lv.")
