import math

MAGNOLIAS_PRICE = 3.25
HYACINTHS_PRICE = 4
ROSES_PRICE = 3.50
CACTI_PRICE = 8.00
TAXES_PERCENT = 5 / 100

magnolias_count = int(input())
hyacinths_count = int(input())
roses_count = int(input())
cacti_count = int(input())
gift_price = float(input())

total_income = magnolias_count * MAGNOLIAS_PRICE + \
               hyacinths_count * HYACINTHS_PRICE + \
               roses_count * ROSES_PRICE + \
               cacti_count * CACTI_PRICE

total_income_after_taxes = total_income * (1 - TAXES_PERCENT)

if total_income_after_taxes >= gift_price:
    print(f"She is left with {math.floor(total_income_after_taxes - gift_price)} leva.")
else:
    print(f"She will have to borrow {math.ceil(gift_price - total_income_after_taxes)} leva.")
