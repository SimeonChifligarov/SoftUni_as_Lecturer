tournaments_count = int(input())
starting_points = int(input())

gained_points = 0
count_wins = 0
for _ in range(tournaments_count):
    result = input()  # "W", "F", or "SF"
    if result == "W":
        gained_points += 2000
        count_wins += 1
    elif result == "F":
        gained_points += 1200
    elif result == "SF":
        gained_points += 720

total_points = starting_points + gained_points
average_points = gained_points / tournaments_count
percent_wins = count_wins / tournaments_count

print(f"Final points: {total_points}")
print(f"Average points: {int(average_points)}")
print(f"{percent_wins :.2%}")

