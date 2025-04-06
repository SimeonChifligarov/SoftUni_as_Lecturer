# print('it works fine')

# for el in collection:  # ...
#     body of for-cycle

# # 1.
# for i in range(2, 7, 2):  # [2, 4, 6]
#     print(i)

# # 2.
# for ch in 'Simo':  # ['S', 'i', 'm', 'o']
#     print(ch)


# name = input()
# while name != 'End':
#     if name == 'Nakov':
#         print('bug here')
#         name = input()
#         continue
#
#     print(f'Hell0, mr. {name}!')
#
#     name = input()
#

# while True:
#     name = input()
#
#     if name == 'End':
#         break
#
#     if name == 'Nakov':
#         print('Will skip "hello" with Nakov')
#         continue
#
#     print(f'Hell0, mr. {name}!')
# import time


# should_break = False
# for week in range(1, 5):  # [1, 2, 3, 4]
#     # time.sleep(1)
#     print(f'Current week - {week}!')
#
#     for day in range(1, 8):  # [1, 2, 3, 4, 5, 6, 7]
#         # time.sleep(1)
#         print(f' ---> Day: {day}')
#
#         if week == 2 and day == 3:
#             should_break = True
#             break
#
#     if should_break:
#         break
#
#     # print('end of current week!')

# should_break = False
# for i in range(10):
#     for j in range(5):
#         for k in range(5):
#             if i == 3 and j == 2 and k == 4:
#                 print('will break with i=3, j=2, k=4')
#                 should_break = True
#                 break
#             print(i, j, k)
#
#         if should_break:
#             break
#
#     if should_break:
#         break

# number = 9876
# number_as_str = str(number)  # str(9876) == '9876'
#
# for d in number_as_str:  # '9876' ~~ ['9', '8', '7', '6']
#     # print(d)
#     # print(type(d))
#     d_as_int = int(d)  # int('9') == 9
#
#     print(1000 * d_as_int)

# name = 'Simeon'
#
# # counter = 0
# # for ch in name:
# #     print(f'{ch} is in position - {counter}')
# #     counter += 1
#
# for idx, ch in enumerate(name):  # [ (0, 'S'), (1, 'i'), (2, 'm')... (5, 'n') ]
#                                  # [ (0, '9'), (1, '8') ... ]
#     print(f'{ch} is in position - {idx}')

# print('line1')  # end='\n'
# print('line2', end='\n\n')
# # print()  # print('', end='\n')
# print('line3')

# print('line1', 'line2', 'line3', sep='###', end=' *** ')

# num = 7
# num = 12
#
# is_prime = True
# for divisor in range(2, num):  # [2, 3, 4, 5, 6]
#     if num % divisor == 0:
#         is_prime = False
#         break
#
# print(is_prime)

# number = 16
#
# num = 2409
# is_special = True
#
# num_as_str = str(num)  # str(2418) == '2418'
# for d in num_as_str:  # ['2', '4', '1', '8']
#     d_as_int = int(d)  # int('2') == 2
#
#     if d_as_int == 0:
#         is_special = False
#         break
#
#     if number % d_as_int != 0:
#         is_special = False
#         break
#
# print(is_special)

# print(16 / 0)  # ZeroDivisionError: division by zero
# print(16 % 0)  # ZeroDivisionError: integer division or modulo by zero
