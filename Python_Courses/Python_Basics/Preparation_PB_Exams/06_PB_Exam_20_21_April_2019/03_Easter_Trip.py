destinations = {
    "France": {
        "21-23": 30,
        "24-27": 35,
        "28-31": 40,
    },
    "Italy": {
        "21-23": 28,
        "24-27": 32,
        "28-31": 39,
    },
    "Germany": {
        "21-23": 32,
        "24-27": 37,
        "28-31": 43,
    },
}

destination = input()  # "France", "Italy", or "Germany"
dates = input()  # "21-23", "24-27", or "28-31"
nights = int(input())

price_per_night = destinations[destination][dates]
total_price = price_per_night * nights

print(f"Easter trip to {destination} : {total_price :.2f} leva.")
