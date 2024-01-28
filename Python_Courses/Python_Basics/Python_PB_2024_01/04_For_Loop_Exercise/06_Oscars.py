actor = input()
starting_points = float(input())
judges_count = int(input())

total_points = starting_points

for _ in range(judges_count):  # [0, 1, 2, ... n - 1]
    judge_name = input()
    judge_points = float(input())
    if total_points <= 1250.5:
        current_points = len(judge_name) * judge_points / 2
        total_points += current_points

if total_points > 1250.5:
    print(f'Congratulations, {actor} got a nominee for leading role with {total_points :.1f}!')
else:
    diff = 1250.5 - total_points
    print(f'Sorry, {actor} you need {diff :.1f} more!')
