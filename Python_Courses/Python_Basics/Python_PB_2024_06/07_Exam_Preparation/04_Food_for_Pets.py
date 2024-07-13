days = int(input())
total_food = float(input())

eaten_biscuits = 0
dog_total_food = 0
cat_total_food = 0
for day in range(1, days + 1):  # [1, 2... days + 1);
    dog_eaten_food = int(input())
    cat_eaten_food = int(input())

    if day % 3 == 0:
        eaten_biscuits += (dog_eaten_food + cat_eaten_food) * 0.10

    dog_total_food += dog_eaten_food
    cat_total_food += cat_eaten_food

total_eaten_food = dog_total_food + cat_total_food
percent_eaten_food = total_eaten_food / total_food * 100
percent_dog_eaten_food = dog_total_food / total_eaten_food * 100
percent_cat_eaten_food = cat_total_food / total_eaten_food * 100

print(f'Total eaten biscuits: {round(eaten_biscuits)}gr.')
print(f'{percent_eaten_food :.2f}% of the food has been eaten.')
print(f'{percent_dog_eaten_food :.2f}% eaten from the dog.')
print(f'{percent_cat_eaten_food :.2f}% eaten from the cat.')
