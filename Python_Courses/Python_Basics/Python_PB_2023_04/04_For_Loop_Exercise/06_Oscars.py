POINTS_NEEDED = 1250.5

actor = input()
starting_points = float(input())
judges_count = int(input())

total_points = starting_points
for _ in range(judges_count):  # [1, 2, 3, 4]; # [0, 1, 2, 3]
    judge_name = input()
    judge_points = float(input())
    total_points += len(judge_name) * judge_points / 2
    if total_points > POINTS_NEEDED:
        print(f"Congratulations, {actor} got a nominee for leading role with {total_points :.1f}!")
        break
else:
    print(f"Sorry, {actor} you need {POINTS_NEEDED - total_points :.1f} more!")
