# •	Пакет химикали - 5.80 лв.
# •	Пакет маркери - 7.20 лв.
# •	Препарат - 1.20 лв (за литър)

# •	Брой пакети химикали - цяло число в интервала [0...100]
pens_packets = int(input())
# •	Брой пакети маркери - цяло число в интервала [0...100]
markers_packets = int(input())
# •	Литри препарат за почистване на дъска - цяло число в интервала [0…50]
cleaning_liters = int(input())
# •	Процент намаление - цяло число в интервала [0...100]
discount_percent = int(input())

money_needed = pens_packets * 5.80 \
               + markers_packets * 7.20 \
               + cleaning_liters * 1.20

money_needed_after_discount = money_needed * (1 - discount_percent / 100)

print(money_needed_after_discount)
