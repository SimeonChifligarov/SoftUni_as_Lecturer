scores = {
    "Wins": 0,
    "Loses": 0,
    "Draws": 0,
}

first_score = input()  # e.g. 1:0
second_score = input()
third_score = input()

for score in (first_score, second_score, third_score):
    team_goals, opponent_goals = [int(el) for el in score.split(":")]
    if team_goals > opponent_goals:
        scores["Wins"] += 1
    elif team_goals == opponent_goals:
        scores["Draws"] += 1
    else:
        scores["Loses"] += 1

# print(scores)

print(f"Team won {scores['Wins']} games.")
print(f"Team lost {scores['Loses']} games.")
print(f"Drawn games: {scores['Draws']}")
