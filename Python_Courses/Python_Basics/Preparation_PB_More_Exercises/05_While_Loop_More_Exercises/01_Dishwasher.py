DISHWASHER_DETERGENT_ML = 750
DISH_NEEDED_ML = 5
POT_NEEDED_ML = 15
END_COMMAND = "End"

dishes_count = 0
pots_count = 0

detergent_bottles = int(input())
detergent_ml = detergent_bottles * DISHWASHER_DETERGENT_ML
is_enough = True

current_load = 0
command = input()
while not command == END_COMMAND:
    current_dishes_or_pots = int(command)
    current_load += 1
    if current_load % 3 == 0:
        detergent_ml -= current_dishes_or_pots * POT_NEEDED_ML
        pots_count += current_dishes_or_pots
    else:
        detergent_ml -= current_dishes_or_pots * DISH_NEEDED_ML
        dishes_count += current_dishes_or_pots

    if detergent_ml < 0:
        is_enough = False
        break
    command = input()

if is_enough:
    print("Detergent was enough!")
    print(f"{dishes_count} dishes and {pots_count} pots were washed.")
    print(f"Leftover detergent {detergent_ml} ml.")
else:
    print(f"Not enough detergent, {-detergent_ml} ml. more necessary!")
