# # Solution 1
# hearthstone_count = 0
# fornite_count = 0
# overwatch_count = 0
# others_count = 0
#
# games_sold = int(input())
# for _ in range(games_sold):
#     game = input()
#     if game == "Hearthstone":
#         hearthstone_count += 1
#     elif game == "Fornite":
#         fornite_count += 1
#     elif game == "Overwatch":
#         overwatch_count += 1
#     else:
#         others_count += 1
#
#
# print(f"Hearthstone - {hearthstone_count / games_sold :.2%}")
# print(f"Fornite - {fornite_count / games_sold :.2%}")
# print(f"Overwatch - {overwatch_count / games_sold :.2%}")
# print(f"Others - {others_count / games_sold :.2%}")

# #########################################################################
# # Solution 2

games_count = {
    "Hearthstone": 0,
    "Fornite": 0,
    "Overwatch": 0,
    "Others": 0,  # this will fail if game name is "Others"
}

games_sold = int(input())
for _ in range(games_sold):
    game = input()
    if game in games_count:
        games_count[game] += 1
    else:
        games_count["Others"] += 1

for game_name, game_count in games_count.items():
    print(f"{game_name} - {game_count / games_sold :.2%}")
