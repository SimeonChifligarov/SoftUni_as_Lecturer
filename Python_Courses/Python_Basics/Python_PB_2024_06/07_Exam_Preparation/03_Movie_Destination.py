budget = float(input())
destination = input()  # "Dubai", "Sofia", or "London"
season = input()  # "Summer" or "Winter"
days = int(input())

cost_per_day = 0
if season == 'Summer':
    if destination == 'Dubai':
        cost_per_day = 40_000
    elif destination == 'Sofia':
        cost_per_day = 12_500
    elif destination == 'London':
        cost_per_day = 20_250
elif season == 'Winter':
    if destination == 'Dubai':
        cost_per_day = 45_000
    elif destination == 'Sofia':
        cost_per_day = 17_000
    elif destination == 'London':
        cost_per_day = 24_000

total_price = days * cost_per_day
if destination == 'Dubai':
    total_price *= 0.70  # total_price = total_price * (1 - 0.30)
elif destination == 'Sofia':
    total_price *= 1.25

if budget >= total_price:
    diff = budget - total_price
    print(f'The budget for the movie is enough! We have {diff :.2f} leva left!')
else:
    diff = total_price - budget
    print(f'The director needs {diff :.2f} leva more!')
