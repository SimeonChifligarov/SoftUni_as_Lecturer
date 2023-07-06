num_of_balls = int(input())
total_points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
other_balls = 0

for ball in range(1, num_of_balls + 1):
    color_of_ball = input()
    if color_of_ball == "red":
        red_balls += 1
        total_points += 5
    elif color_of_ball == "orange":
        orange_balls += 1
        total_points += 10
    elif color_of_ball == "yellow":
        yellow_balls += 1
        total_points += 15
    elif color_of_ball == "white":
        white_balls += 1
        total_points += 20
    elif color_of_ball == "black":
        black_balls += 1
        total_points /= 2
    else:
        other_balls += 1

print(f'Total points: {int(total_points)}')
print(f'Red balls: {red_balls}')
print(f'Orange balls: {orange_balls}')
print(f'Yellow balls: {yellow_balls}')
print(f'White balls: {white_balls}')
print(f'Other colors picked: {other_balls}')
print(f'Divides from black balls: {black_balls}')
