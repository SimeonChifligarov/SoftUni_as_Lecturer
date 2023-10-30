target_amount = float(input())

# [2lv, 1lv, 50st, 20st, 10st, 5st, 2st, 1st]
# [200st, 100st, 50st, 20st, 10st, 5st, 2st, 1st]

target_amount_pennies = int(target_amount * 100)

coins_count = 0
while target_amount_pennies > 0:
    coins_count += 1

    if target_amount_pennies >= 200:
        target_amount_pennies -= 200
    elif target_amount_pennies >= 100:
        target_amount_pennies -= 100
    elif target_amount_pennies >= 50:
        target_amount_pennies -= 50
    elif target_amount_pennies >= 20:
        target_amount_pennies -= 20
    elif target_amount_pennies >= 10:
        target_amount_pennies -= 10
    elif target_amount_pennies >= 5:
        target_amount_pennies -= 5
    elif target_amount_pennies >= 2:
        target_amount_pennies -= 2
    elif target_amount_pennies >= 1:
        target_amount_pennies -= 1

print(coins_count)
