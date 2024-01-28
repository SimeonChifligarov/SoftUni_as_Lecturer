# print('it\'s all right')

# outside_var = 'Simo'
#
# for i in range(0, 5, 1):  # [0, 1, 2, 3, 4]
#     print(f'Current value of i - {i}')
#     print(type(i))
#     print('i will repeat this action')
#     print(f'outside var - {outside_var}')
#
# # print('---')
# # print(f'i value outside for loop - {i}')


# help(range)

# 1.
# for number in range(5):  # [0, 1, 2, 3, 4]
#     print(number)
#     print('--- end of iteration')

# for i in range(5, 10):  # [5, 6, 7, 8, 9]
#     print(i)
#     print('--- end of iteration')

# for i in range(1, 25, 3):  # [1, 4, 7, ..., 22]
#     print(i)
#

# for letter in 'Simo':  # ['S', 'i', 'm', 'o']
#     print(letter)

# for num in range(10):
#     print(num)
#     if num == 5:
#         break
#
#     print('here')
#
#
# print('outside for loop')

# break

# ll = ['simo', 'is', 'lector']
# for word in ll:
#     print(word)
#     print('---')

# text = "I am feeling good"  # type str
#
# text_2 = '12345678'
# print(len(text))  # 17
#
# print(text_2[0])  # "a"
# print(text_2[2])  # "a"
# print(text_2[5])  # "a"
#
# print('Stefan'[1])

# for i in range(10):  # [0, 1, ... 9]
#     print(i)
#     if i == 15:
#         break
# else:
#     print('for loop gone through all the elements')
#
#
# print('outside for loop')

# database_name = 'user_info'
#
# for attempt in range(1, 6):  # [1, 2, 3, 4, 5]
#     print(f'Attempt No {attempt}')
#     database_name = f'DATABASE{attempt}'
#     if attempt == 3:
#         print('Success!!!')
#         break
#
#     print(f'Trying to connect to DataBase - {database_name}...')
#
# print(database_name)
#
# for num in range(20000, 400, 2):  # []
#     print(num)
#     print('here')
#
# print('outside')

# number = int(input())
# #
# my_var = 0
# if number >= 10:
#     my_var = 'greater than 10'
# else:
#     my_var_2 = 'less than 10'
#
# print(my_var)

# for i in range(10):
#     my_var = 10
#
# print(my_var)

# text = '    '
# print(len(text))

# for char in 'I am':
#     print(f' -> current char is: ${char}$')

# for _ in range(5):
#     print('do some action 1')
#     print('do some action 2')

# discount = 0.7
#
# print(f'$ -> {discount :.3%}')
# import math
#
# num = 2.899999
#
# # print(num // 1)
# print(math.floor(num))
# print(int(num))

is_break_hit = False
for num in range(4):  # [0, 1, 2, 3]
    print('here')
    if num == 2:
        is_break_hit = True
        break

if not is_break_hit:
    print('for cycle goes without break')
else:
    print('break was hit')


