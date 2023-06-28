movies_count = 0
others_count = 0

voucher_value = int(input())

voucher_left = voucher_value
command = input()
while command != "End":
    purchase = command
    if len(purchase) > 8:
        purchase_cost = ord(purchase[0]) + ord(purchase[1])
        if purchase_cost <= voucher_left:
            movies_count += 1
    else:
        purchase_cost = ord(purchase[0])
        if purchase_cost <= voucher_left:
            others_count += 1

    voucher_left -= purchase_cost
    if voucher_left < 0:
        break

    command = input()

print(movies_count)
print(others_count)
