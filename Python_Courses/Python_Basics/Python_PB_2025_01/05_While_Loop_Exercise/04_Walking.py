total_steps = 0
# 1. init
command = input()  # 'Going home' or steps as a string, e.g. '1000'
# 2. check
while command != 'Going home':
    steps = int(command)  # int('1000') == 1000
    total_steps += steps

    if total_steps >= 10_000:
        break

    # 3. change
    command = input()

if command == 'Going home':
    home_steps = int(input())
    total_steps += home_steps

is_goal_achieved = total_steps >= 10_000
if is_goal_achieved:
    diff = total_steps - 10_000
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    diff = 10_000 - total_steps
    print(f'{diff} more steps to reach goal.')
