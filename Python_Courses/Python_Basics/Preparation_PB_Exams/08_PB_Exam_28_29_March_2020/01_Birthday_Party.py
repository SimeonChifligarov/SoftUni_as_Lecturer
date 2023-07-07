hall_rent = float(input())
cake_price = hall_rent * 0.20
drinks_price = cake_price * (1 - 0.45)
animator_price = hall_rent / 3

total_cost = hall_rent + cake_price + drinks_price + animator_price
print(total_cost)
