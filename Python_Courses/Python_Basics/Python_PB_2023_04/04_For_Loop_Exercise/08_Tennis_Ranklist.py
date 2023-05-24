import math

W_POINTS = 2000
F_POINTS = 1200
SF_POINTS = 720

tournaments_count = int(input())
starting_points = int(input())

gained_points = 0
total_wins = 0
for _ in range(tournaments_count):
    tournament_result = input()  # "W", "F" или "SF"
    if tournament_result == "W":
        gained_points += W_POINTS
        total_wins += 1
    elif tournament_result == "F":
        gained_points += F_POINTS
    elif tournament_result == "SF":
        gained_points += SF_POINTS

total_points = starting_points + gained_points
avg_points = math.floor(gained_points / tournaments_count)
wins_percent = total_wins / tournaments_count * 100

print(f"Final points: {total_points}")
print(f"Average points: {avg_points}")
print(f"{wins_percent :.2f}%")
