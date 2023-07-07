prices = {
    "m": {
        "Gym": 42,
        "Boxing": 41,
        "Yoga": 45,
        "Zumba": 34,
        "Dances": 51,
        "Pilates": 39,
    },
    "f": {
        "Gym": 35,
        "Boxing": 37,
        "Yoga": 42,
        "Zumba": 31,
        "Dances": 53,
        "Pilates": 37,
    },
}

budget = float(input())
gender = input()  # "m" or "f"
age = int(input())
sport = input()  # "Gym", "Boxing", "Yoga", "Zumba", "Dances", "Pilates"

price = prices[gender][sport]
if age <= 19:
    price *= (1 - 0.20)

if budget >= price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${price - budget :.2f} more.")
