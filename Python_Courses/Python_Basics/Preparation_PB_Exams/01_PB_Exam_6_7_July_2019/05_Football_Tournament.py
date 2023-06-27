football_stats = {
    # "_football_club": {
    #     "games_count": 0,
    #     "W": 0,
    #     "L": 0,
    #     "D": 0,
    #     "win_rate": 0,
    #     "points": 0,
    # },
}

football_club = input()
football_stats[football_club] = {
    "games_count": 0,
    "W": 0,
    "L": 0,
    "D": 0,
    "win_rate": 0,
    "points": 0,
}

games_count = int(input())
for _ in range(games_count):
    result = input()  # 'W', 'D' и 'L'
    football_stats[football_club][result] += 1

if games_count != 0:
    football_stats[football_club]["games_count"] = games_count
    football_stats[football_club]["win_rate"] = football_stats[football_club]["W"] \
                                                / football_stats[football_club]["games_count"]
    football_stats[football_club]["points"] = football_stats[football_club]["W"] * 3 \
                                              + football_stats[football_club]["D"] * 1

if games_count == 0:
    print(f"{football_club} hasn't played any games during this season.")
else:
    print(f"{football_club} has won {football_stats[football_club]['points']} points during this season.")
    print("Total stats:")
    print(f"## W: {football_stats[football_club]['W']}")
    print(f"## D: {football_stats[football_club]['D']}")
    print(f"## L: {football_stats[football_club]['L']}")
    print(f"Win rate: {football_stats[football_club]['win_rate'] :.2%}")
