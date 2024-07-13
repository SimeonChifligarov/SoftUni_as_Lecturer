prices_per_day = {
    "Dubai": {
        "Summer": 40_000,
        "Winter": 45_000,
    },
    "Sofia": {
        "Summer": 12_500,
        "Winter": 17_000,
    },
    "London": {
        "Summer": 20_250,
        "Winter": 24_000,
    },
}

budget = float(input())
destination = input()  # "Dubai", "Sofia", or "London"
season = input()  # "Summer" or "Winter"
days = int(input())

price_per_day = prices_per_day[destination][season]
money_needed = price_per_day * days

if destination == "Dubai":
    money_needed *= (1 - 0.30)
elif destination == "Sofia":
    money_needed *= (1 + 0.25)

if budget >= money_needed:
    print(f"The budget for the movie is enough! We have {budget - money_needed :.2f} leva left!")
else:
    print(f"The director needs {money_needed - budget :.2f} leva more!")
