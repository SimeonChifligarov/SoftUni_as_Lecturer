players = []

command = input()
while not command == "Stop":
    player_name = command
    player_points = 0
    for i in range(len(player_name)):
        current_guess = int(input())
        if current_guess == ord(player_name[i]):
            player_points += 10
        else:
            player_points += 2

    player = {"name": player_name, "points": player_points}
    players.append(player)

    command = input()

players.sort(key=lambda p: p['points'])
# print(players)
best_player = players[-1]

print(f"The winner is {best_player['name']} with {best_player['points']} points!")
