steps_goal = 10_000

total_steps = 0
while True:
    command = input()

    if command == 'Going home':
        extra_steps = int(input())
        total_steps += extra_steps
        break

    current_steps = int(command)
    total_steps += current_steps
    if total_steps >= steps_goal:
        break

if total_steps >= steps_goal:
    diff = total_steps - steps_goal
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    diff = steps_goal - total_steps
    print(f'{diff} more steps to reach goal.')
