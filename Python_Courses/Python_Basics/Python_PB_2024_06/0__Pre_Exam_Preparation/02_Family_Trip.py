budget = float(input())
nights = int(input())
night_price = float(input())
additional_costs_percent = int(input())

additional_costs = additional_costs_percent / 100

nights_cost = nights * night_price
if nights > 7:
    nights_cost *= 0.95

additional_costs = budget * additional_costs
budget_left = budget
budget_left -= nights_cost + additional_costs

if budget_left >= 0:
    print(f"Ivanovi will be left with {budget_left :.2f} leva after vacation.")
else:
    print(f"{-budget_left :.2f} leva needed.")
