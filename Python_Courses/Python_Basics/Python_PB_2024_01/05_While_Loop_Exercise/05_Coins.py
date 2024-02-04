# [2lv, 1lv, 50st, 20st, 10st, 5st, 2st, 1st]

change = float(input())

coins = 0
change_left = change
while change_left > 0:
    if change_left >= 2:
        change_left -= 2
    elif change_left >= 1:
        change_left -= 1
    elif change_left >= 0.50:
        change_left -= 0.50
    elif change_left >= 0.20:
        change_left -= 0.20
    elif change_left >= 0.10:
        change_left -= 0.10
    elif change_left >= 0.05:
        change_left -= 0.05
    elif change_left >= 0.02:
        change_left -= 0.02
    elif change_left >= 0.01:
        change_left -= 0.01

    coins += 1
    change_left = round(change_left, 2)

print(coins)
