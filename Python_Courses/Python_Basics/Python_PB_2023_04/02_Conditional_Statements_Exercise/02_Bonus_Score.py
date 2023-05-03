STARTING_BONUS_POINTS = 0

LOWER_BOUND_VALUE = 100
UPPER_BOUND_VALUE = 1000

LOWER_BOUND_BONUS_POINTS = 5
BETWEEN_LOWER_AND_UPPER_BOUND_BONUS_POINTS_MULTIPLIER = 0.20
UPPER_BOUND_BONUS_POINTS_MULTIPLIER = 0.10

BONUS_POINTS_FOR_EVEN = 1
BONUS_POINTS_FOR_ENDING_WITH_5 = 2

starting_number = int(input())


bonus_points = STARTING_BONUS_POINTS
if starting_number <= LOWER_BOUND_VALUE:
    bonus_points = bonus_points + LOWER_BOUND_BONUS_POINTS
elif starting_number <= UPPER_BOUND_VALUE:
    bonus_points = bonus_points + starting_number * BETWEEN_LOWER_AND_UPPER_BOUND_BONUS_POINTS_MULTIPLIER
else:
    bonus_points = bonus_points + starting_number * UPPER_BOUND_BONUS_POINTS_MULTIPLIER

if starting_number % 2 == 0:
    bonus_points = bonus_points + BONUS_POINTS_FOR_EVEN

if starting_number % 10 == 5:
    bonus_points = bonus_points + BONUS_POINTS_FOR_ENDING_WITH_5

total_points = starting_number + bonus_points

print(bonus_points)
print(total_points)
