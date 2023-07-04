flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs_dozens = int(input())
yeast_count = int(input())

sugar_price = flour_price * (1 - 0.25)
eggs_price = flour_price * (1 + 0.10)
yeast_price = sugar_price * (1 - 0.80)

total_price = flour_price * flour_kg + sugar_price * sugar_kg + eggs_price * eggs_dozens + yeast_price * yeast_count
print(f"{total_price :.2f}")
