total_steps = 0

while True:
    command = input()  # 'Going home' or steps_as_str

    if command == 'Going home':
        steps_home = int(input())
        total_steps += steps_home
        break

    current_steps = int(command)  # int('1300') == 1300

    total_steps += current_steps
    if total_steps >= 10_000:
        break

is_goal_achieved = total_steps >= 10_000

if is_goal_achieved:
    steps_over = total_steps - 10_000
    print('Goal reached! Good job!')
    print(f'{steps_over} steps over the goal!')
else:
    steps_needed = 10_000 - total_steps
    print(f'{steps_needed} more steps to reach goal.')
