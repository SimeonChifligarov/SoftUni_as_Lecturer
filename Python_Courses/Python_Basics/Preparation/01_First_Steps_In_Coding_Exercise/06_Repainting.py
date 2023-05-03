NYLON = 1.50
PAINT = 14.50
PAINT_THINNER = 5.00
BAGS_TOTAL = 0.40

nylon_quantity = int(input())
paint_quantity = int(input())
paint_thinner_quantity = int(input())
work_hours = int(input())

materials_needed = nylon_quantity * NYLON + paint_quantity * PAINT + paint_thinner_quantity * PAINT_THINNER
materials_extra = paint_quantity * PAINT * 0.10 + NYLON * 2 + BAGS_TOTAL

materials_total = materials_needed + materials_extra
work_expenses_per_hour = materials_total * 0.30
work_expenses_total = work_expenses_per_hour * work_hours

total_expenses = materials_total + work_expenses_total

print(total_expenses)
