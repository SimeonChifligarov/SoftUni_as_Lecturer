p1_eggs = int(input())
p2_eggs = int(input())

loser = None
command = input()
while command != "End":
    winner = command
    if winner == "one":
        p2_eggs -= 1
        if p2_eggs <= 0:
            loser = 'two'
            break
    elif winner == "two":
        p1_eggs -= 1
        if p1_eggs <= 0:
            loser = 'one'
            break

    command = input()

if loser:
    winner_eggs = max(p1_eggs, p2_eggs)
    winner_player = 'one' if loser == 'two' else 'two'
    print(f"Player {loser} is out of eggs. Player {winner_player} has {winner_eggs} eggs left.")
else:
    print(f"Player one has {p1_eggs} eggs left.")
    print(f"Player two has {p2_eggs} eggs left.")
