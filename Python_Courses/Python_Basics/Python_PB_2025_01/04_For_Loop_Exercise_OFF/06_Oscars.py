POINTS_NEEDED = 1250.5

actor = input()
academy_points = float(input())
judges_count = int(input())

total_points = academy_points
for _ in range(judges_count):
    judge_name = input()
    judge_points = float(input())
    actual_points = len(judge_name) * judge_points / 2
    total_points += actual_points
    if total_points > POINTS_NEEDED:
        print(f"Congratulations, {actor} got a nominee for leading role with {total_points :.1f}!")
        break
else:
    print(f"Sorry, {actor} you need {POINTS_NEEDED - total_points :.1f} more!")
