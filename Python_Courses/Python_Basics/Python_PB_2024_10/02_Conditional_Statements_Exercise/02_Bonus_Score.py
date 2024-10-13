starting_points = int(input())

bonus_points = 0
if starting_points <= 100:
    bonus_points = 5
elif starting_points <= 1000:
    bonus_points = starting_points * 0.20
else:
    bonus_points = starting_points * 0.10

addition_bonus_points = 0
if starting_points % 2 == 0:
    addition_bonus_points = 1

if starting_points % 10 == 5:
    addition_bonus_points = 2

total_bonus = bonus_points + addition_bonus_points
total_result = starting_points + total_bonus

print(total_bonus)
print(total_result)
