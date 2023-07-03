STARTING_POINTS = 301

fields = {
    "Single": 1,
    "Double": 2,
    "Triple": 3,
}

player = input()

player_remaining_points = STARTING_POINTS
is_winner = False
successful_shots = 0
unsuccessful_shots = 0

command = input()
while command != "Retire":
    field = command  # "Single", "Double", or "Triple"
    points = int(input())

    current_points = fields[field] * points
    if current_points <= player_remaining_points:
        successful_shots += 1
        player_remaining_points -= current_points
        if player_remaining_points == 0:
            is_winner = True
            break
    else:
        unsuccessful_shots += 1

    command = input()

if is_winner:
    print(f"{player} won the leg with {successful_shots} shots.")
else:
    print(f"{player} retired after {unsuccessful_shots} unsuccessful shots.")
