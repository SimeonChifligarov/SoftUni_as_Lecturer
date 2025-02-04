import math

W_POINTS = 2000
F_POINTS = 1200
SF_POINTS = 720

tournaments_count = int(input())
starting_points = int(input())

gained_points = 0
win_count = 0
for _ in range(tournaments_count):
    tournament_finish = input()  # "W", "F" или "SF"
    if tournament_finish == "W":
        gained_points += W_POINTS
        win_count += 1
    elif tournament_finish == "F":
        gained_points += F_POINTS
    elif tournament_finish == "SF":
        gained_points += SF_POINTS

total_points = starting_points + gained_points
avg_points = gained_points / tournaments_count
win_percent = win_count / tournaments_count * 100
print(f"Final points: {total_points}")
print(f"Average points: {math.floor(avg_points)}")
print(f"{win_percent :.2f}%")
