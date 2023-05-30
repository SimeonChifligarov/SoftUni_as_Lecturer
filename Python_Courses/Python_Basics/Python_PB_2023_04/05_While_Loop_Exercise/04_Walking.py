steps = 0

command = input()  # "Going home" OR "55"
while command != "Going home":
    current_steps = int(command)
    steps += current_steps
    if steps >= 10_000:
        break

    command = input()


if command == "Going home":
    current_steps = int(input())
    steps += current_steps

if steps >= 10_000:
    print("Goal reached! Good job!")
    print(f"{steps - 10_000} steps over the goal!")
else:
    print(f"{10_000 - steps} more steps to reach goal.")
