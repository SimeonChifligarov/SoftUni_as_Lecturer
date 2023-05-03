PENS_PRICE = 5.80
MARKERS_PRICE = 7.20
CLEANING_MATERIAL_PRICE = 1.20

pens_count = int(input())
markers_count = int(input())
cleaning_material_liters = int(input())
discount_percent = int(input())

total_sum = pens_count * PENS_PRICE \
            + markers_count * MARKERS_PRICE\
            + cleaning_material_liters * CLEANING_MATERIAL_PRICE

total_sum_with_discount = total_sum * (100 - discount_percent) / 100

print(total_sum_with_discount)
