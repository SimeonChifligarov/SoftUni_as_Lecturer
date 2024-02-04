# [2lv, 1lv, 50st, 20st, 10st, 5st, 2st, 1st]
# [200st, 100st, 50st, ...]
change_amount = float(input())  # 1.23

change_amount_pennies = int(change_amount * 100)  # 123
total_coins = 0

while change_amount_pennies > 0:
    if change_amount_pennies >= 200:
        change_amount_pennies -= 200
    elif change_amount_pennies >= 100:
        change_amount_pennies -= 100
    elif change_amount_pennies >= 50:
        change_amount_pennies -= 50
    elif change_amount_pennies >= 20:
        change_amount_pennies -= 20
    elif change_amount_pennies >= 10:
        change_amount_pennies -= 10
    elif change_amount_pennies >= 5:
        change_amount_pennies -= 5
    elif change_amount_pennies >= 2:
        change_amount_pennies -= 2
    elif change_amount_pennies >= 1:
        change_amount_pennies -= 1

    total_coins += 1

print(total_coins)
