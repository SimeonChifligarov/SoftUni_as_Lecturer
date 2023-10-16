celsius = int(input())
time_of_day = input()

suit = ""
shoes = ""
if time_of_day == "Morning":
    if 10 <= celsius <= 18:
        suit = "Sweatshirt"
        shoes = "Sneakers"
        print(f"It's {celsius} degrees, get your {suit} and {shoes}.")
    elif 18 < celsius <= 24:
        suit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {celsius} degrees, get your {suit} and {shoes}.")
    elif celsius >= 25:
        suit = "T-Shirt"
        shoes = "Sandals"
        print(f"It's {celsius} degrees, get your {suit} and {shoes}.")
if time_of_day == "Afternoon":
    if 10 <= celsius <= 18:
        suit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {celsius} degrees, get your {suit} and {shoes}.")
    elif 18 < celsius <= 24:
        suit = "T-Shirt"
        shoes = "Sandals"
        print(f"It's {celsius} degrees, get your {suit} and {shoes}.")
    elif celsius >= 25:
        suit = "Swim Suit"
        shoes = "Barefoot"
        print(f"It's {celsius} degrees, get your {suit} and {shoes}.")
if time_of_day == "Evening":
    if 10 <= celsius <= 18:
        suit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {celsius} degrees, get your {suit} and {shoes}.")
    elif 18 < celsius <= 24:
        suit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {celsius} degrees, get your {suit} and {shoes}.")
    elif celsius >= 25:
        suit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {celsius} degrees, get your {suit} and {shoes}.")
