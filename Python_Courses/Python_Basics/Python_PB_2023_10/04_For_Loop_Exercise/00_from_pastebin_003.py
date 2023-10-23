month = input()
number_of_spent_nights = int(input())

studio_price_for_night = 0
apartment_price_for_night = 0
if month == "May" or month == "October":
    studio_price_for_night = 50
    apartment_price_for_night = 65
elif month == "June" or month == "September":
    studio_price_for_night = 75.20
    apartment_price_for_night = 68.70
elif month == "July" or month == "August":
    studio_price_for_night = 76
    apartment_price_for_night = 77
total_price_for_apartment = apartment_price_for_night * number_of_spent_nights
total_price_for_studio = studio_price_for_night * number_of_spent_nights
discount_for_studio = 0
discount_for_apartment = 0
if month == "May" or month == "October":
    if 7 < number_of_spent_nights <= 14:
        discount_for_studio = total_price_for_studio * 0.05
    elif number_of_spent_nights > 14:
        discount_for_studio = total_price_for_studio * 0.30
        discount_for_apartment = total_price_for_apartment * 0.10
elif month == "June" or month == "September":
    if number_of_spent_nights > 14:
        discount_for_studio = total_price_for_studio * 0.20
        discount_for_apartment = total_price_for_apartment * 0.10
elif month == "July" or month == "August":
    if number_of_spent_nights > 14:
        discount_for_apartment = total_price_for_apartment * 0.10
final_price_for_apartment = total_price_for_apartment - discount_for_apartment
final_price_for_studio = total_price_for_studio - discount_for_studio
print(f"Apartment: {final_price_for_apartment:.2f} lv.")
print(f"Studio: {final_price_for_studio:.2f} lv.")
