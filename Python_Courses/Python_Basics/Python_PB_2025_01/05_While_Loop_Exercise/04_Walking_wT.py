total_steps = 0
while True:
    command = input()  # 'Going home' or steps as a string

    if command == 'Going home':
        home_steps = int(input())
        total_steps += home_steps
        break

    current_steps = int(command)  # NOT input()
    total_steps += current_steps

    if total_steps >= 10_000:
        break

is_goal_achieved = total_steps >= 10_000
if is_goal_achieved:
    diff = total_steps - 10_000
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    diff = 10_000 - total_steps
    print(f'{diff} more steps to reach goal.')