total_cost = 0

days = int(input())
hours_per_day = int(input())

for d in range(1, days + 1):
    day_cost = 0
    for h in range(1, hours_per_day + 1):
        if d % 2 == 0 and h % 2 != 0:
            day_cost += 2.50
        elif d % 2 != 0 and h % 2 == 0:
            day_cost += 1.25
        else:
            day_cost += 1.00

    print(f"Day: {d} - {day_cost :.2f} leva")
    total_cost += day_cost

print(f"Total: {total_cost :.2f} leva")
