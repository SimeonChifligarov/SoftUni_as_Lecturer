# •	Предпазен найлон - 1.50 лв. за кв. метър
# •	Боя - 14.50 лв. за литър
# •	Разредител за боя - 5.00 лв. за литър

# 1. E
nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
hours_needed = int(input())

# 2. T
paint_needed_total = paint_needed * 1.10  # +10%
nylon_needed_total = nylon_needed + 2  # +2
bag_price = 0.40  # +0.40 lv

total_materials_price = paint_needed_total * 14.50 + nylon_needed_total * 1.50 + thinner_needed * 5.00 + bag_price
total_work_price = hours_needed * 0.30 * total_materials_price

total_price = total_materials_price + total_work_price

# 3. L
print(total_price)
