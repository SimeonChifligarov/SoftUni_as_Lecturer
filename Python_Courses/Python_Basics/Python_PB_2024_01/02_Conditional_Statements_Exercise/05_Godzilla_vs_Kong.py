budget = float(input())
walk_on_count = int(input())
clothes_cost_per_walk_on = float(input())

# •	Декорът за филма е на стойност 10% от бюджета.
scene_cost = budget * 0.10
# •	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.
if walk_on_count > 150:
    # clothes_cost_per_walk_on = clothes_cost_per_walk_on * (1 - 0.10)
    clothes_cost_per_walk_on *= 0.90  # clothes_cost_per_walk_on = clothes_cost_per_walk_on * 0.90

total_cost = scene_cost + walk_on_count * clothes_cost_per_walk_on

difference = budget - total_cost
if difference < 0:
    print(f'Not enough money!\nWingard needs {abs(difference) :.2f} leva more.')
else:
    print(f'Action!\nWingard starts filming with {difference :.2f} leva left.')
