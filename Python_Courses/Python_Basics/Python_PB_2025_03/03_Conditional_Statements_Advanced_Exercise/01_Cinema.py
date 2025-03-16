# •	Premiere - премиерна прожекция, на цена 12.00 лева;
# •	Normal - стандартна прожекция, на цена 7.50 лева;
# •	Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.

projection_type = input()
rows = int(input())
columns = int(input())

ticket_price = 0.0
if projection_type == 'Premiere':
    ticket_price = 12.00
elif projection_type == 'Normal':
    ticket_price = 7.50
elif projection_type == 'Discount':  # else:
    ticket_price = 5.00

full_capacity = rows * columns
total_income = full_capacity * ticket_price

print(f'{total_income:.2f} leva')  # 2047.50 leva
