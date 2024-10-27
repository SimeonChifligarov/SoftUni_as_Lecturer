# W - ако е победител получава 2000 точки
# F - ако е финалист получава 1200 точки
# SF - ако е полуфиналист получава 720 точки

tournaments_count = int(input())
starting_point = int(input())

points_gained = 0
tournaments_win = 0
for _ in range(tournaments_count):  # [0, 1, 2, 3]
    current_result = input()  # "W", "F", "SF"
    if current_result == 'W':
        points_gained += 2000
        tournaments_win += 1
    elif current_result == 'F':
        points_gained += 1200
    elif current_result == 'SF':
        points_gained += 720


final_score = starting_point + points_gained
average_points_gained = points_gained / tournaments_count
percent_win = tournaments_win / tournaments_count * 100

print(f"Final points: {final_score}")
print(f"Average points: {int(average_points_gained)}")  # math.floor
print(f"{percent_win :.2f}%")
