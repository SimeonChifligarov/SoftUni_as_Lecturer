import math

w_points = 2000
f_points = 1200
sf_points = 720

tournaments_counts = int(input())
starting_points = int(input())

gained_points = 0
total_wins = 0

for _ in range(tournaments_counts):
    tournament_result = input()  # w_points , f_points , sf_points
    if tournament_result == "W":
        gained_points += w_points
        total_wins += 1
    elif tournament_result == "F":
        gained_points += f_points
    elif tournament_result == "SF":
        gained_points += sf_points

total_points = starting_points + gained_points
avg_points = math.floor(gained_points / tournaments_counts)
wins_percent = total_wins / tournaments_counts * 100

print(f"Final points: {total_points}")
print(f"Average points: {avg_points}")
print(f"{wins_percent :.2f}%")