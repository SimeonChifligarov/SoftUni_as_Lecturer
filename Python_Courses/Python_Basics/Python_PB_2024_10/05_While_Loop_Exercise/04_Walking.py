steps_goal = 10_000

current_steps = 0

# 1. init
command = input()  # 'Going home' or steps as a str (e.g. '1000')

# 2. check
while command != 'Going home':
    steps = int(command)  # int('1000') == 1000

    current_steps += steps
    # if current_steps >= 10_000:
    if current_steps >= steps_goal:
        break

    # 3. potential change
    command = input()

if command == 'Going home':
    extra_steps = int(input())
    current_steps += extra_steps

if current_steps >= steps_goal:
    diff = current_steps - steps_goal
    print('Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
else:
    diff = steps_goal - current_steps
    print(f'{diff} more steps to reach goal.')
