# print('hello here ;)')

# name = input()
# while name != "End":
#     if name == "Nakov":
#         print(f'Will skip this one with {name}')
#         name = input()
#         continue
#     print(f'Hello {name}!')
#
#     name = input()

# for i in range(1, 7, 0.5):
#     print(i)

# i = 1
# while i < 7:
#     print(i)
#     i += 0.5


# num = 1
# if num is 1:
#     print('something')

# i = 0
# while i == 0:
#     print("SoftUni")
#     if i == 1:
#         break

# i = 0
# while i <= 6:
#     if i % 2 == 0:
#         print(i, end="")
#     i += 1

# i = 0
#
# while i < 5:
#   if i == 0:
#     print(i)
#     break
#   i += 1

# import time
#
# for week in range(1, 5):
#     time.sleep(1)
#     print(f'Week {week}')
#     for day in range(1, 8):  # [1, ... 7]
#         time.sleep(1)
#         print(f'---> Day - {day}!')


# for hour in range(0, 3):  # [0, 1... 23]
#     for minute in range(0, 5):
#         for seconds in range(0, 10):
#             print(f'{hour:02d}:{minute}:{seconds}')

# hour = 1
# for minute in range(0, 5):
#     print(f'{hour}:{minute}')

# combination_count = 0
#
# for x1 in range(0, 5+1):
#     for x2 in range(0, 5+1):
#         for x3 in range(0, 5+1):
#             if x1 + x2 + x3 == 5:
#                 print(f'valid combination: {x1}+{x2}+{x3}=5')
#                 combination_count += 1
#
# print(f'total combinations: {combination_count}')

# import time
#
# should_break = False
# for week in range(1, 5):
#     # time.sleep(1)
#     print(f'Week {week}')
#     for day in range(1, 8):  # [1, ... 7]
#         if day == 3 and week == 3:
#             should_break = True
#             break
#         # time.sleep(1)
#         print(f'---> Day - {day}!')
#
#     if should_break:
#         break
# should_break = False
# for h in range(24):
#     for m in range(60):
#         for s in range(60):
#             if h == 3 and m == 30 and s == 22:
#                 should_break = True
#                 break
#             print(f'{h}:{m}:{s}')
#
#         if should_break:
#             break
#     if should_break:
#         break

for h in range(24):  # [0 ... 24]
    for m in range(60):  # [0...24]
        print(f'{h}:{m}')
