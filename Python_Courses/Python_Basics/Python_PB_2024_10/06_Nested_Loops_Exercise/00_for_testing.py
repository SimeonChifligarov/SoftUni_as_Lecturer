# # # # print('it w0rkz! ')
# # #
# # # name = input()
# # # while name != 'End':
# # #     if name == 'Nakov':
# # #         print('Will skip this iteration')
# # #         name = input()
# # #         continue
# # #     print(f'Hell0, {name}!!!')
# # #     name = input()
# #
# # import time
# #
# #
# # for week in range(1, 5):  # [1, 2, 3, 4]
# #     should_break = False
# #     time.sleep(1)
# #     print(f'Current week is - {week}!')
# #
# #     for day in range(1, 8):  # [1, ..., 7]
# #         time.sleep(1)
# #
# #         if week == 3 and day == 4:
# #             should_break = True
# #             break
# #
# #         print(f' ---> Day No {day}')
# #
# #     if should_break:
# #         break
# #
# # # while True:
# # #     name = input()
# # #
# # #     if name == 'End':
# # #         break
# # #
# # #     if name == 'Nakov':
# # #         pass
# # #
# # #     print(f'...')
# #
# #
# #
#
#
# should_break = False
#
# for i in range(10):
#     print('i')
#     for j in range(5):
#         print('j')
#         for k in range(5):
#             print('k')
#             if i == 4 and j == 3 and k == 2:
#                 print(f'Will break with i={i}, j={j}, k={k}')
#                 should_break = True
#                 break
#
#         if should_break:
#             break
#             # print(i, j, k)
#     if should_break:
#         break

# print('line1', end='***')
# print('line2', end='***')
# print()  # print('', end='\n')
# print('line3', end='***')
# i = 22
# j = 33
# # print('{0}{1}'.format(i,j), end="")
#
# print(f'{i}{j}')

# num = 9876
#
# num_as_string = str(num)  # str(9876) == '9876'
#
# # counter = 0
# # for d in num_as_string:  # ['9', '8', '7', '6']
# #     print(f'current digit - {d}, index - {counter}')
# #     counter += 1
#
# for idx, dig in enumerate(num_as_string):  # [ (0, '9') , (1, '8') , (2, '7') , (3, '6') ]
#     print(f'current digit - {dig}, index - {idx}')
#     print(type(idx))
#     print(type(dig))
#
#     dig_as_num = int(dig)  # 9
#     print(f'converted value - {type(dig_as_num)}')
#
#     print(dig_as_num % 2 == 0)  # True
#     # print(dig % 2 == 0)  # Error

# number = 3
number = 9

is_prime = True
for divisor in range(2, number):  # [2, 3, 4, ... number-1]  == [2, ]  # [2, ... 8]
    if number % divisor == 0:
        is_prime = False
        break

print(f'Number {number} is prime = {is_prime}')
