# steps = 0
#
# is_achieved = False
#
# # "Going home" OR integer as string, e.g. "2000"
# while not is_achieved:
#     command = input()
#     if command == "Going home":
#         to_home_steps = int(input())
#         steps += to_home_steps
#         break
#
#     current_steps = int(command)  # e.g. int("2000") => 2000
#     steps += current_steps
#     if steps >= 10000:
#         is_achieved = True
#
#
# if steps >= 10000:
#     print("Goal reached! Good job!")
#     print(f"{steps - 10000} steps over the goal!")
# else:
#     print(f"{10000 - steps} more steps to reach goal.")

steps = 0

command = input()
while command != "Going home":
    current_steps = int(command)
    steps += current_steps
    if steps >= 10000:
        break

    command = input()

if command == "Going home":
    current_steps = int(input())
    # #L37 -> int("Going home") => ValueError: invalid literal for int() with base 10: 'Going home'
    steps += current_steps

if steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{steps - 10000} steps over the goal!")
else:
    print(f"{10000 - steps} more steps to reach goal.")
