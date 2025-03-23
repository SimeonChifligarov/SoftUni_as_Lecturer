actor_name = input()
starting_points = float(input())
judges_count = int(input())

current_points = starting_points
for _ in range(judges_count):  # [0, 1, 2, 3...]
    judge_name = input()
    judge_points = float(input())

    judge_result = len(judge_name) * judge_points / 2
    current_points += judge_result
    if current_points > 1250.5:
        break

if current_points > 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {current_points:.1f}!')
else:
    points_needed = 1250.5 - current_points
    print(f'Sorry, {actor_name} you need {points_needed:.1f} more!')
