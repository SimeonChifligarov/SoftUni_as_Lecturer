food_available = int(input()) * 1000

is_food_enough = True
command = input()
while command != "Adopted":
    food_for_the_day = int(command)
    food_available -= food_for_the_day
    if food_available < 0:
        is_food_enough = False
    command = input()

if is_food_enough:
    print(f"Food is enough! Leftovers: {food_available} grams.")
else:
    print(f"Food is not enough. You need {-food_available} grams more.")
