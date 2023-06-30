discounts = {
    "Thrones": 0.50,
    "Lucifer": 0.40,
    "Protector": 0.30,
    "TotalDrama": 0.20,
    "Area": 0.10,
}

budget_total = float(input())

budget_left = budget_total
series_count = int(input())
for _ in range(series_count):
    series_name = input()
    series_price = float(input())
    if series_name in discounts:
        discount = discounts[series_name]
        series_price *= (1 - discount)

    budget_left -= series_price

if budget_left < 0:
    print(f"You need {-budget_left :.2f} lv. more to buy the series!")
else:
    print(f"You bought all the series and left with {budget_left :.2f} lv.")
