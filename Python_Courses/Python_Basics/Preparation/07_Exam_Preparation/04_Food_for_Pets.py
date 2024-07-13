total_eaten_biscuits = 0
total_dog_eaten = 0
total_cat_eaten = 0

days = int(input())
total_food_quantity = float(input())

for d in range(1, days + 1):
    dog_eaten_food = int(input())
    cat_eaten_food = int(input())

    total_dog_eaten += dog_eaten_food
    total_cat_eaten += cat_eaten_food

    if d % 3 == 0:
        eaten_biscuits = (dog_eaten_food + cat_eaten_food) * 0.10
        total_eaten_biscuits += eaten_biscuits

total_eaten = total_dog_eaten + total_cat_eaten

print(f"Total eaten biscuits: {round(total_eaten_biscuits)}gr.")
print(f"{total_eaten / total_food_quantity :.2%} of the food has been eaten.")
print(f"{total_dog_eaten / total_eaten :.2%} eaten from the dog.")
print(f"{total_cat_eaten / total_eaten :.2%} eaten from the cat.")
