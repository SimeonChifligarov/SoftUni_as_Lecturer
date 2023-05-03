STARTING_BONUS_POINTS = 0
LOWER_LIMIT = 100
UPPER_LIMIT = 1000

BONUS_FOR_LESS_THAN_LOWER_LIMIT_AS_RULE = 5
BONUS_FOR_BETWEEN_LOWER_AND_UPPER_LIMIT_AS_MULTIPLIER = 0.2
BONUS_FOR_MORE_THAN_UPPER_LIMIT_AS_MULTIPLIER = 0.1

BONUS_FOR_EVEN = 1
BONUS_FOR_ENDING_WITH_FIVE = 2

starting_points = int(input())

bonus_points = STARTING_BONUS_POINTS
if starting_points <= LOWER_LIMIT:
    bonus_points = BONUS_FOR_LESS_THAN_LOWER_LIMIT_AS_RULE
elif starting_points <= UPPER_LIMIT:
    bonus_points = starting_points * BONUS_FOR_BETWEEN_LOWER_AND_UPPER_LIMIT_AS_MULTIPLIER
else:
    bonus_points = starting_points * BONUS_FOR_MORE_THAN_UPPER_LIMIT_AS_MULTIPLIER

if starting_points % 2 == 0:
    bonus_points += BONUS_FOR_EVEN

if starting_points % 10 == 5:
    bonus_points += BONUS_FOR_ENDING_WITH_FIVE

total_points = starting_points + bonus_points

print(bonus_points)
print(total_points)
