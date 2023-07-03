total_wins = 0
total_losses = 0

command = input()
while command != "End of tournaments":
    tournament = command
    games_count = int(input())
    for game in range(1, games_count + 1):
        team_points = int(input())
        opponent_points = int(input())
        if team_points > opponent_points:
            total_wins += 1
            print(f"Game {game} of tournament {tournament}: win with {team_points - opponent_points} points.")
        elif opponent_points > team_points:
            total_losses += 1
            print(f"Game {game} of tournament {tournament}: lost with {opponent_points - team_points} points.")

    command = input()

total_games = total_wins + total_losses
print(f"{total_wins / total_games :.2%} matches win")
print(f"{total_losses / total_games :.2%} matches lost")
