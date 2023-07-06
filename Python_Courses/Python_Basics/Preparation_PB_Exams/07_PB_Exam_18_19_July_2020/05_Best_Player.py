best_player = ""
best_player_goals = 0

command = input()
while command != "END":
    player = command
    goals = int(input())
    if goals > best_player_goals:
        best_player_goals = goals
        best_player = player

    if goals >= 10:
        break

    command = input()

print(f"{best_player} is the best player!")
if best_player_goals >= 3:
    print(f"He has scored {best_player_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_player_goals} goals.")
