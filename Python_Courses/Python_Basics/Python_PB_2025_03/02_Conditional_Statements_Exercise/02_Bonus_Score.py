# 1.
starting_points = int(input())

# 2.
bonus_points = 0
if starting_points <= 100:  # (-inf; 100]
    bonus_points = 5
elif starting_points <= 1000:  # (100; 1000]
    bonus_points = starting_points * 0.20
else:  # elif starting_points > 1000:  # (1000; +inf)
    bonus_points = starting_points * 0.10

extra_bonus_points = 0
if starting_points % 2 == 0:
    extra_bonus_points = 1
elif starting_points % 10 == 5:  # 1337 % 10 == 7
    extra_bonus_points = 2

total_bonus_points = bonus_points + extra_bonus_points

total_points = starting_points + total_bonus_points
# 3.
print(total_bonus_points)
print(total_points)
