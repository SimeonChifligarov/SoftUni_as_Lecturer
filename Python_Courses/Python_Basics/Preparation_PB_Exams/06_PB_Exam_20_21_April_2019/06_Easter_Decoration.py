prices = {
    "basket": 1.50,
    "wreath": 3.80,
    "chocolate bunny": 7.00,
}

total_bill = 0

customers = int(input())
for _ in range(customers):
    customer_purchases = 0
    customer_bill = 0
    command = input()
    while command != "Finish":
        customer_purchases += 1
        purchase = command  # "basket", "wreath", or "chocolate bunny"
        price = prices[purchase]
        customer_bill += price
        command = input()
    if customer_purchases % 2 == 0:
        customer_bill *= (1 - 0.20)

    total_bill += customer_bill
    print(f"You purchased {customer_purchases} items for {customer_bill :.2f} leva.")

print(f"Average bill per client is: {total_bill / customers :.2f} leva.")
