prices = {
    "Large": {
        "Red": 16,
        "Green": 12,
        "Yellow": 9,
    },
    "Medium": {
        "Red": 13,
        "Green": 9,
        "Yellow": 7,
    },
    "Small": {
        "Red": 9,
        "Green": 8,
        "Yellow": 5,
    },
}

eggs_size = input()  # "Large", "Medium", or "Small"
eggs_color = input()  # "Red", "Green", or "Yellow"
eggs_batches = int(input())

price = prices[eggs_size][eggs_color]
total_income = price * eggs_batches
total_expense = total_income * 0.35
total_profit = total_income - total_expense

print(f"{total_profit :.2f} leva.")
