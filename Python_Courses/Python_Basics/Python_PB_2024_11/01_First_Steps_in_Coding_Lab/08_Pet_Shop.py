# храна за кучета е на цена 2.50 лв
# а опаковка храна за котки струва 4 лв.

dogs_eat_count = int(input())
cats_eat_count = int(input())

total_price = dogs_eat_count * 2.50 + cats_eat_count * 4

print(f'{total_price} lv.')
