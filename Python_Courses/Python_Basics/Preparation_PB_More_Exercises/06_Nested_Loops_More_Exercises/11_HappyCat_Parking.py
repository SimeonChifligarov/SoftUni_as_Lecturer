days_count = int(input())
hours_per_day = int(input())

# всеки четен ден и нечетен час, паркингът таксува 2.50 лева.
# Във всеки нечетен ден и четен час таксата е 1.25 лева,
# във всички останали случаи се заплаща 1 лев.
total_price = 0
for d in range(1, days_count + 1):
    day_price = 0
    for h in range(1, hours_per_day + 1):
        if d % 2 == 0 and h % 2 != 0:
            day_price += 2.50
        elif d % 2 != 0 and h % 2 == 0:
            day_price += 1.25
        else:
            day_price += 1

    total_price += day_price
    print(f"Day: {d} - {day_price :.2f} leva")

print(f"Total: {total_price :.2f} leva")
