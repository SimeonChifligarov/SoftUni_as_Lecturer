command = input()
total_steps = 0
is_goal_achieved = False

while command != 'Going home':
    current_steps = int(command)

    total_steps += current_steps
    if total_steps >= 10000:
        break

    command = input()

if command == 'Going home':
    steps_home = int(input())
    total_steps += steps_home

is_goal_achieved = total_steps >= 10000

if is_goal_achieved:
    steps_over = total_steps - 10000
    print("Goal reached! Good job!")
    print(f'{steps_over} steps over the goal!')
else:
    steps_needed = 10000 - total_steps
    print(f"{steps_needed} more steps to reach goal.")
