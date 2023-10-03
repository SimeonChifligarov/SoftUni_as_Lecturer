NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
PAINT_THINNER_PRICE = 5.00
BAG_PRICE = 0.40

nylon_quantity = int(input())
paint_quantity = int(input())
paint_thinner_quantity = int(input())
work_hours_needed = int(input())

nylon_extra_quantity = 2
paint_extra_quantity = 0.10 * paint_quantity

total_material_price = (nylon_quantity + nylon_extra_quantity) * NYLON_PRICE \
                       + (paint_quantity + paint_extra_quantity) * PAINT_PRICE \
                       + paint_thinner_quantity * PAINT_THINNER_PRICE \
                       + BAG_PRICE

work_per_hours_price = total_material_price * 0.30

total_price = total_material_price + work_per_hours_price * work_hours_needed

print(total_price)
