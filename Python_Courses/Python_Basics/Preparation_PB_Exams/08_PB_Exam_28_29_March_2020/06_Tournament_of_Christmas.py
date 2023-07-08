MONEY_PER_WIN = 20

win_days = 0
lose_days = 0
total_money = 0

days = int(input())

for _ in range(days):
    day_money = 0
    sport_wins = 0
    sport_losses = 0
    command = input()
    while command != "Finish":
        sport = command
        result = input()  # "win" or "lose"
        if result == "win":
            day_money += MONEY_PER_WIN
            sport_wins += 1
        elif result == "lose":
            sport_losses += 1

        command = input()

    if sport_wins > sport_losses:
        day_money *= (1 + 0.10)
        win_days += 1
    else:
        lose_days += 1

    total_money += day_money

if win_days > lose_days:
    total_money *= (1 + 0.20)
    print(f"You won the tournament! Total raised money: {total_money :.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money :.2f}")
