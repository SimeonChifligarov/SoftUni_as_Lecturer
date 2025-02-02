# possible coins = 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01

change = float(input())

total_coins = 0
while change > 0:

    if change >= 2:
        change -= 2
    elif change >= 1:
        change -= 1
    elif change >= 0.50:
        change -= 0.50
    elif change >= 0.20:
        change -= 0.20
    elif change >= 0.10:
        change -= 0.10
    elif change >= 0.05:
        change -= 0.05
    elif change >= 0.02:
        change -= 0.02
    elif change >= 0.01:
        change -= 0.01

    change = round(change, 2)
    total_coins += 1

print(total_coins)
