GOAL_STEPS = 10_000
total_steps = 0
# is_goal_achieved = False

# 1. init
command = input()  # 'Going home' OR steps_as_str e.g. '1300'
# 2. check condition
while command != 'Going home':
    current_steps = int(command)  # e.g. int('1300') == 1300

    total_steps += current_steps
    if total_steps >= GOAL_STEPS:
        # is_goal_achieved = True
        break

    command = input()  # 3. potential change

if command == 'Going home':
    steps_home = int(input())
    total_steps += steps_home
    # if total_steps >= 10_000:
    #     is_goal_achieved = True

is_goal_achieved = total_steps >= GOAL_STEPS

if is_goal_achieved:
    steps_over = total_steps - GOAL_STEPS
    print('Goal reached! Good job!')
    print(f'{steps_over} steps over the goal!')
else:
    steps_needed = GOAL_STEPS - total_steps
    print(f'{steps_needed} more steps to reach goal.')
