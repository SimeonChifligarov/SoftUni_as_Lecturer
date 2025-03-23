import math

tournaments_count = int(input())
starting_points = int(input())

gained_points = 0
wins_count = 0
for _ in range(tournaments_count):
    current_result = input()  # 'W', 'F', 'SF'

    if current_result == 'W':
        gained_points += 2000
        wins_count += 1
    elif current_result == 'F':
        gained_points += 1200
    elif current_result == 'SF':  # else:
        gained_points += 720

final_points = starting_points + gained_points
avg_points = gained_points / tournaments_count
wins_percent = wins_count / tournaments_count * 100

print(f'Final points: {final_points}')
print(f'Average points: {math.floor(avg_points)}')
print(f'{wins_percent:.2f}%')
