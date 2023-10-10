starting_points = int(input())  # check this casting if not 100% score

bonus_points = 0
if starting_points <= 100:
    bonus_points = 5
elif 1000 >= starting_points > 100:  # (100; 1000]
    bonus_points = 0.20 * starting_points
# elif starting_points > 1000:  # (1000; ...)
else:
    bonus_points = 0.10 * starting_points

if starting_points % 2 == 0:
    bonus_points = bonus_points + 1

if starting_points % 10 == 5:
    bonus_points = bonus_points + 2

print(bonus_points)
print(starting_points + bonus_points)
