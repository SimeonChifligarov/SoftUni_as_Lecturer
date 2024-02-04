# goal = 10_000

total_steps = 0

command = input()  # either command 'Going home', or steps (as string), e.g. '2000'
while command != 'Going home':
    current_steps = int(command)
    total_steps += current_steps

    if total_steps >= 10_000:
        break

    command = input()


# if command == 'Going home':
else:
    current_steps = int(input())
    total_steps += current_steps

is_goal_reached = total_steps >= 10_000

if is_goal_reached:
    diff = total_steps - 10_000
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    diff = 10_000 - total_steps
    print(f'{diff} more steps to reach goal.')
