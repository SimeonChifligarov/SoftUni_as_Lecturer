EASTER_BREAD_PRICE = 3.20
EGGS_PRICE = 4.35
COOKIES_PRICE = 5.40
EGG_PAINT = 0.15

easter_bread_count = int(input())
eggs_dozens = int(input())
cookies_kg = int(input())

total_cost = easter_bread_count * EASTER_BREAD_PRICE \
             + eggs_dozens * EGGS_PRICE + eggs_dozens * 12 * EGG_PAINT \
             + cookies_kg * COOKIES_PRICE

print(f"{total_cost :.2f}")
