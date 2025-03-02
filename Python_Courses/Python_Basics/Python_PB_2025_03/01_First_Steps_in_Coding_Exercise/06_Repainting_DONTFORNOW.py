NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
SOLVENT_PRICE = 5.00
BAG_PRICE = 0.40

# 1. E
nylon_needed = int(input())
paint_needed = int(input())
solvent_needed = int(input())
hours_needed = int(input())

# 2. T
paint_needed_total = paint_needed * 1.10  # +10%
nylon_needed_total = nylon_needed + 2  # +2
# bag_price = 0.40  # +0.40 lv

total_materials_price = (
        paint_needed_total * PAINT_PRICE
        + nylon_needed_total * NYLON_PRICE
        + solvent_needed * SOLVENT_PRICE
        + BAG_PRICE
)

total_work_price = hours_needed * 0.30 * total_materials_price

total_price = total_materials_price + total_work_price

# 3. L
print(total_price)
