# •	На първия ред е месецът -
# •	На втория ред е броят на нощувките - цяло число.


month = input()  # May, June, July, August, September или October;
nights = int(input())

studio_price_per_night = 0
apartment_price_per_night = 0
if month == "May" or month == "October":
    studio_price_per_night = 50
    apartment_price_per_night = 65
    if 7 < nights <= 14:
        studio_price_per_night *= 0.95
    elif nights > 14:
        studio_price_per_night *= 0.70  # (1 - 0.30)
    # if nights > 14:
    #     studio_price_per_night *= 0.70
    # elif nights > 7:  # nights are between (7; 14]
    #     studio_price_per_night *= 0.95
elif month == "June" or month == "September":
    studio_price_per_night = 75.20
    apartment_price_per_night = 68.70
    if nights > 14:
        studio_price_per_night *= 0.80
elif month == "July" or month == "August":
    studio_price_per_night = 76
    apartment_price_per_night = 77

if nights > 14:
    apartment_price_per_night *= 0.90

studio_total_cost = nights * studio_price_per_night
apartment_total_cost = nights * apartment_price_per_night

print(f"Apartment: {apartment_total_cost :.2f} lv.")
print(f"Studio: {studio_total_cost :.2f} lv.")
