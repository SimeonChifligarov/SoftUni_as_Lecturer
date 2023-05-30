STEPS_GOAL = 10_000
GOING_HOME_COMMAND = "Going home"

total_steps = 0

while True:
    command = input()
    if command == GOING_HOME_COMMAND:
        steps_to_home = int(input())
        total_steps += steps_to_home
        break

    current_steps = int(command)
    total_steps += current_steps

    if total_steps >= STEPS_GOAL:
        break

is_goal_achieved = total_steps >= STEPS_GOAL
if is_goal_achieved:
    print("Goal reached! Good job!")
    print(f"{total_steps - STEPS_GOAL} steps over the goal!")
else:
    print(f"{STEPS_GOAL - total_steps} more steps to reach goal.")
