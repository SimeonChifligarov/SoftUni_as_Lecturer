cinema_type = input()
r = int(input())
c = int(input())

capacity = r * c

price = 0.0
if cinema_type == 'Premiere':
    price = 12.00
elif cinema_type == 'Normal':
    price = 7.50
elif cinema_type == 'Discount':
    price = 5.00

total_price = capacity * price

print(f'{total_price :.2f} leva')
