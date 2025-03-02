# 1. E
annual_fee = int(input())

# 2. T
sneakers = annual_fee * 0.60  # annual_fee * (1 - 0.40)
equip = sneakers * 0.80  # sneakers * (1 - 0.20)
ball = equip * 0.25  # equip * 1 / 4
accessoirs = ball * 0.20  # ball * 1 / 5

final_price = annual_fee + sneakers + equip + ball + accessoirs

# 3. L
print(final_price)
