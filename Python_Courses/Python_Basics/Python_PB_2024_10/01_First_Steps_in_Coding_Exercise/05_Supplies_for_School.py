# •	Пакет химикали - 5.80 лв.
# •	Пакет маркери - 7.20 лв.
# •	Препарат - 1.20 лв (за литър)
# PENS_PRICE = 5.80

pens_packets = int(input())
markers_packets = int(input())
thinner_liters = int(input())
discount_percent = int(input())  # int('25') == 25

total_price = pens_packets * 5.80 + markers_packets * 7.20 + thinner_liters * 1.20
total_price_after_discount = total_price * (1 - discount_percent / 100)  # 250 * (1 - 0.25) == 250 * 0.75

print(total_price_after_discount)
