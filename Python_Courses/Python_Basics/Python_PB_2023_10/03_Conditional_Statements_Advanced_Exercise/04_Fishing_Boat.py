budget = int(input())
season = input()  # "Spring", "Summer", "Autumn" или "Winter"
fishermen = int(input())

boat_rent = 0
discount = 0
if season == "Spring":
    boat_rent = 3000
elif season == "Summer" or season == "Autumn":
    boat_rent = 4200
elif season == "Winter":  # else:
    boat_rent = 2600

if fishermen <= 6:
    discount = 0.10
    # boat_rent *= 0.90  # boat_rent = boat_rent * (1 - 0.10) eq. boat_rent = boat_rent * 0.90
elif fishermen <= 11:  # [7; 11]
    discount = 0.15
else:  # elif fishermen >= 12:
    discount = 0.25

extra_discount = 0
# if fishermen % 2 == 0 and not season == "Autumn":  # eq "... and season != "Autumn""
if fishermen % 2 == 0 and (season == "Spring" or season == "Summer" or season == "Winter"):  # eq "... and season != "Autumn""
    extra_discount = 0.05

total_cost = boat_rent * (1 - discount) * (1 - extra_discount)  # != boat_rent * (1 - discount - extra_discount)

diff = budget - total_cost
if diff >= 0:
    print(f"Yes! You have {abs(diff) :.2f} leva left.")  # 100 => abs(100) == 100
else:
    print(f"Not enough money! You need {abs(diff) :.2f} leva.")  # eq. {-diff :.2f}
