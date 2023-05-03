CHICKEN_PRICE = 10.35
FISH_PRICE = 12.40
VEG_PRICE = 8.15
DELIVERY_PRICE = 2.50

chicken_count = int(input())
fish_count = int(input())
veg_count = int(input())

total_price_without_dessert = chicken_count * CHICKEN_PRICE + fish_count * FISH_PRICE + veg_count * VEG_PRICE
dessert_price = total_price_without_dessert * 0.20

total_price = total_price_without_dessert + dessert_price + DELIVERY_PRICE

print(total_price)
