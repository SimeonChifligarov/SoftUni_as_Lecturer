month = input()  # May, June, July, August, September или October
nights = int(input())

studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if 14 >= nights > 7:
        studio_price *= 0.95
    elif nights > 14:
        studio_price *= 0.70
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if nights > 14:
        studio_price *= 0.80
elif month == "July" or month == "August":
    studio_price = 76.00
    apartment_price = 77.00

if nights > 14:
    apartment_price *= 0.90

apartment_total_price = nights * apartment_price
studio_total_price = nights * studio_price
print(f"Apartment: {apartment_total_price :.2f} lv.")
print(f"Studio: {studio_total_price :.2f} lv.")
