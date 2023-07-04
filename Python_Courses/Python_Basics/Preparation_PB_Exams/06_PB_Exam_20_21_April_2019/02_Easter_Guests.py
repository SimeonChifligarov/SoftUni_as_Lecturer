import math

EASTER_BREAD_PRICE = 4.00
EGG_PRICE = 0.45

guests = int(input())
budget = int(input())

easter_bread_needed = math.ceil(guests / 3)
eggs_needed = guests * 2

money_needed = easter_bread_needed * EASTER_BREAD_PRICE + eggs_needed * EGG_PRICE

if budget >= money_needed:
    print(f"Lyubo bought {easter_bread_needed} Easter bread and {eggs_needed} eggs.")
    print(f"He has {budget - money_needed :.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {money_needed - budget :.2f} lv. more.")
