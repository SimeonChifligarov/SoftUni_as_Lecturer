# •	Premiere - премиерна прожекция, на цена 12.00 лева;
# •	Normal - стандартна прожекция, на цена 7.50 лева;
# •	Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.

type_projection = input()
rows = int(input())
cols = int(input())

ticket_price = 0.0
if type_projection == 'Premiere':
    ticket_price = 12.00
elif type_projection == 'Normal':
    ticket_price = 7.50
elif type_projection == 'Discount':  # else:
    # else:
    ticket_price = 5.00

capacity = rows * cols  # 3r * 5c == 15

total_income = capacity * ticket_price

print(f'{total_income:.2f} leva')
