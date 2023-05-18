# # Solution 1 => should be refactored
#
# distance = int(input())
# day_or_night = input()  # “day” или “night”
#
# price_min = 0
# if day_or_night == "day":
#     price_taxi = 0.70 + 0.79 * distance
#     if distance < 20:
#         price_min = price_taxi
#     elif distance < 100:
#         price_bus = 0.09 * distance
#         price_min = min(price_taxi, price_bus)
#     elif distance >= 100:
#         price_bus = 0.09 * distance
#         price_train = 0.06 * distance
#         price_min = min(price_taxi, price_bus, price_train)
# elif day_or_night == "night":
#     price_taxi = 0.70 + 0.90 * distance
#     if distance < 20:
#         price_min = price_taxi
#     elif distance < 100:
#         price_bus = 0.09 * distance
#         price_min = min(price_taxi, price_bus)
#     elif distance >= 100:
#         price_bus = 0.09 * distance
#         price_train = 0.06 * distance
#         price_min = min(price_taxi, price_bus, price_train)
#
# print(f"{price_min :.2f}")

# Solution 2 => using hints from word doc

distance = int(input())
day_or_night = input()  # “day” или “night”

min_price = 0
if distance < 20:
    if day_or_night == "day":
        min_price = 0.70 + 0.79 * distance
    elif day_or_night == "night":
        min_price = 0.70 + 0.90 * distance
elif distance < 100:
    min_price = 0.09 * distance
else:
    min_price = 0.06 * distance

print(f"{min_price :.2f}")
