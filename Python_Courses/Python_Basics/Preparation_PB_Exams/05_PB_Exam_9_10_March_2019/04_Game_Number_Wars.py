p1_score = 0
p2_score = 0

player_1 = input()
player_2 = input()

is_ended = False
command = input()
while command != "End of game":
    p1_card = int(command)
    p2_card = int(input())
    if p1_card == p2_card:
        is_ended = True
        print("Number wars!")

        p1_card = int(input())
        p2_card = int(input())
        if p1_card > p2_card:  # it is guaranteed that p1_card will not be equal to p2_card
            print(f"{player_1} is winner with {p1_score} points")
        elif p2_card > p1_card:
            print(f"{player_2} is winner with {p2_score} points")
        break

    if p1_card > p2_card:
        p1_score += p1_card - p2_card
    else:
        p2_score += p2_card - p1_card

    command = input()

if not is_ended:
    print(f"{player_1} has {p1_score} points")
    print(f"{player_2} has {p2_score} points")
