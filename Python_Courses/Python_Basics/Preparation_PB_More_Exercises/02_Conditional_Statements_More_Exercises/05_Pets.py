import math

days = int(input())
food_kgs = int(input())
dog_kgs_per_day = float(input())
cat_kgs_per_day = float(input())
turtle_kgs_per_day = float(input()) / 1000

total_food_needed = days * (dog_kgs_per_day + cat_kgs_per_day + turtle_kgs_per_day)

if total_food_needed <= food_kgs:
    print(f"{math.floor(food_kgs - total_food_needed)} kilos of food left.")
else:
    print(f"{math.ceil(total_food_needed - food_kgs)} more kilos of food are needed.")
