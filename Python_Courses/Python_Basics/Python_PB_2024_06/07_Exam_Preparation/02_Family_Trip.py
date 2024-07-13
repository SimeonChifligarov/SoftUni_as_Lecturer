budget = float(input())
nights = int(input())
night_price = float(input())
additional_cost_percent = int(input())

if nights > 7:
    night_price *= 0.95  # night_price * (1 - 0.05)

nights_price = nights * night_price
additional_cost = budget * additional_cost_percent / 100

total_price = nights_price + additional_cost  # 1.02; 1 + 2 == 3

if budget >= total_price:
    diff = budget - total_price
    print(f'Ivanovi will be left with {diff :.2f} leva after vacation.')
else:
    diff = total_price - budget  # diff = abs(budget - total_price)
    print(f'{diff :.2f} leva needed.')
