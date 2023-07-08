# # Solution 1 -> 1 year ago
# days = int(input())
# total_food = float(input())
#
# dog_eat_real = 0
# cat_eat_real = 0
# dog_biz = 0
# total_eat = 0
#
# for day in range(1, days+1):
#     dog_eat = int(input())
#     cat_eat = int(input())
#     dog_eat_real += dog_eat
#     cat_eat_real += cat_eat
#     day_eat = dog_eat + cat_eat
#     total_eat += day_eat
#     if day % 3 == 0:
#         dog_biz += 0.10 * day_eat
#     day_eat = 0
#
# print(f'Total eaten biscuits: {round(dog_biz)}gr.')
# print(f'{total_eat / total_food * 100:.2f}% of the food has been eaten.')
# print(f'{dog_eat_real / total_eat * 100:.2f}% eaten from the dog.')
# print(f'{cat_eat_real / total_eat * 100:.2f}% eaten from the cat.')
#
# ########################################################
#
#
# Solution 2

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
