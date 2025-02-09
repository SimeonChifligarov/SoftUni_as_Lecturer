# print('it works fine')

# iterations = int(input())
#
# for i in range(iterations):
#     print('iter')


# for i in range(4):  # [0, 1, 2, 3]
#     print(i)

# for char in 'Simo':  # ['S', 'i', 'm', 'o']
#     print(char)

# break

# for i in range(5):
#     print('here')

    # if i == 3:
    #     break

    # if i == 3:
    #     continue
    #
    # print('print after')

# name = input()
# while name != 'End':
#     if name == 'Nakov':
#         print('will skip with Nakov')
#         name = input()
#         continue
#
#     print(f'Hello {name}!')
#
#     name = input()

# while True:
#     name = input()
#
#     if name == 'End':
#         break
#
#     if name == 'Nakov':
#         print('will skip')
#         continue
#
#     print(f'Hello {name}!')

# number = 13.37
#
# number_rounded = round(number, 1)
# print(number_rounded)

# import time
#
#
# for week in range(1, 5):  # [1, 2, 3, 4]
#     time.sleep(1)
#     print(f'Current week -> {week}')
#
#     for day in range(1, 8):  # [1, 2, 3, 4, 5, 6, 7]
#         time.sleep(1)
#         print(f' ---> Day is {day}')

# print(float('3.1416'))
#
# print(float('Simo'))

import time

# should_break = False
# for week in range(1, 5):  # [1, 2, 3, 4]
#     # time.sleep(1)
#     print(f'Current week -> {week}')
#
#     for day in range(1, 8):  # [1, 2, 3, 4, 5, 6, 7]
#         # time.sleep(1)
#
#         if week == 2 and day == 3:
#             should_break = True
#             break
#
#         print(f' ---> Day is {day}')
#
#     if should_break:
#         break

# should_break = False
# for i in range(10):
#     print('i')
#     for j in range(5):
#         print('j')
#         for k in range(5):
#             print('k')
#             if i == 3 and j == 2 and k == 2:
#                 print(f'Will break with i={i}, j={j}, k={k}')
#                 should_break = True
#                 break
#
#         if should_break:
#             break
#
#     if should_break:
#         break

# print('line1')
# print('line2')
# print()  # print('', end='\n')
# print('line3')

# for _ in range(5):
#     number = int(input())

# number = 9876
#
# number_as_str = str(number)  # '9876'
# for d in number_as_str:  # ['9', '8', '7', '6']
#     print(d)
#     print(type(d))
#
#     d_as_num = int(d)  # int('9') == 9
#     print(d_as_num - 3)

# name = 'Simo'
#
# counter = 0
# for ch in name:  # ['S', 'i', 'm', 'o']
#     print(f'char={ch}, idx={counter}')

# for idx, char in enumerate(name):  # [ (0, 'S'), (1, 'i'), (2, 'm'), (3, 'o') ]
#     print(f'char={char}, idx={idx}')
#
# number = 7
#
# is_prime = True
# for divisor in range(2, number):  # [2, 3, 4, 5, 6]
#     if number % divisor == 0:
#         is_prime = False
#         break
#
# print(is_prime)

# for i in range(2, 1):  # []
#     print('zzz')
#
# print('outside for')

# input_number = 16
#
# number = 1113
# number_as_str = str(number)  # '2418'
#
# is_special = True
# for d in number_as_str:  # ['2', '4', '1', '8']
#     d_as_int = int(d)  # int('2') == 2
#
#     if input_number % d_as_int != 0:
#         is_special = False
#         break
#
# print(is_special)
