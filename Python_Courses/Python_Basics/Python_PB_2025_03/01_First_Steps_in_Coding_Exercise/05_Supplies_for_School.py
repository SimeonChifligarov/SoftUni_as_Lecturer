# •	Пакет химикали - 5.80 лв.
# •	Пакет маркери - 7.20 лв.
# •	Препарат - 1.20 лв (за литър)

# 1. E
pens_packets = int(input())
markers_packets = int(input())
thinner_liters = int(input())
discount = int(input())

# 2. T
total_price = pens_packets * 5.80 + markers_packets * 7.20 + thinner_liters * 1.20
discount_percent = discount / 100  # 0.25

total_price_after_discount = total_price * (1 - discount_percent)  # total * (1 - 0.25) == total * 0.75

# 3. L
print(total_price_after_discount)
