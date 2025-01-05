# •	Пакет химикали - 5.80 лв.
# •	Пакет маркери - 7.20 лв.
# •	Препарат - 1.20 лв (за литър)

pens_packets = int(input())  # int('33') == 33
markers_packets = int(input())
thinner_liters = int(input())
discount = int(input())

total_price = pens_packets * 5.80 + markers_packets * 7.20 + thinner_liters * 1.20
discount_price = total_price * discount / 100
total_price_after_discount = total_price - discount_price
# total_price_after_discount = total_price * (1 - discount / 100)  # 1 - 0.15 == 0.85

print(total_price_after_discount)
