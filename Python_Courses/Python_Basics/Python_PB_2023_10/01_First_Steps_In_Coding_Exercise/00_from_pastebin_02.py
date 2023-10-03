NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
PAINT_THINNER_PRICE = 5.00
NYLON_BAG_PRICE = 0.40

nylon_needed = int(input())
paint_needed = int(input())
paint_thinner_needed = int(input())
hours_needed = int(input())

final_nylon_price = (nylon_needed + 2) * NYLON_PRICE
final_paint_price = (paint_needed + 0.10 * paint_needed) * PAINT_PRICE
final_paint_thinner_price = paint_thinner_needed * PAINT_THINNER_PRICE

all_materials_price = final_nylon_price + final_paint_price + final_paint_thinner_price + NYLON_BAG_PRICE
one_hour_work_price = (all_materials_price * 0.30)
full_work_price = one_hour_work_price * hours_needed

full_together_price = all_materials_price + full_work_price
print(full_together_price)