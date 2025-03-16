# print('it is okay as setup ;)')


# num = 100
#
# if num > 50:
#     print('num is greater than 50')
#     if num > 750:
#         print('num is greater than 75')
#
#     print('inside outer if, but not inside inner if')
#
# a = 5


# num = 1000
#
# if num > 500:
#     print('num is greater than 500')
#     print('num is greater than 500')
#     print('num is greater than 500')
#     print('num is greater than 500')
# print('num is greater than 500')
# if num > 75:
#     print('num is greater than 75')

# num = 5
#
# if num > 1:
#     ...
#     if num > 2:
#         ...
#         if num > 3:
#             ...
#
#         ...

# and
# or
# not


# condition_1 -> value; simple check;
# 			-> complex check;

# 1. value check

# num = 100
# if num:  # bool(num) == { True, False }
#     print('num is not zero')

# name = 'Simo'
# name = ''
# name = input()
# if name:
#     print('name is not an empty string')
# else:
#     print('please enter an not empty string')

# # 2. simple check
# num = 100
# if num > 50:
#     print('it is greater than 50')

# 3. complex check -> using and, or, not
# num = 101
#
# if num > 50 and num % 2 == 0:
#     print('num is greater than 50 and num is even')

# # PNAO
#
# print(True or False and False)     # and has precedence
# print((True or False) and False)   # parentheses change precedence
#
# print(not False or True)        # not has precedence
# print(not (False or True))      # parentheses change precedence

# num = 100

# if num > 50 or num % 2 != 0:
#     print('yes')

# is_valid_1 = True  # num > 50
# is_valid_2 = True
# is_not_valid_1 = False
# is_not_valid_2 = False

# print(f'T and T == {True and True}')
# print(f'T and F == {True and False}')
# print(f'F and T == {False and True}')
# print(f'F and F == {False and False}')
#
# print('---')
# print(f'T or T == {True or True}')
# print(f'T or F == {True or False}')
# print(f'F or T == {False or True}')
# print(f'F or F == {False or False}')
#
# print('---')
# print(not(True))
# print(not(False))
#

# result = '3:1'  # 'a:b'
#
# # 'Simo'  # [0 -> 'S', 1 -> 'i', 2 -> 'm', 3 -> 'o']
#
# first_team_goals = int(result[0])  # int('3') == 3
# second_team_goals = int(result[2])
#
# print(first_team_goals)
# print(type(first_team_goals))

# print(f'my name is\tSimo')
# print(f'a\tb')
# print(f'a    b')

# num = 100
# if num > 50:
#     print('line 1')
#     print('line 2')

# customer = 'Simeon'
#
# if customer == 'Georgi' or customer == 'Simo':
#     print('it is Georgi or Simo')

# if customer == 'Georgi':
#     print('it is Georgi or Simo')

# if 'Simo':
#     print('it is Georgi or Simo')

# print('Simo' == 'Simo123')  # False
# print('Simo' in 'Simo123')  # True

# number_1 = 123451337
# number_2 = 123_451_337_222
#
# print(f'{number_2:,}')
# print(type(number_2))
# print(number_1 == number_2)  # True

# num1 = 112
# num2 = 0
#
# print(num1 / num2)

# num = 100
#
# # if num > 50:
# #     print('it is greater than 50')
# # else:
# #     print('it is not greater than 50')
#
# print('it is greater than 50') if num > 50 else print('it is not greater than 50')

# # eval is evil
#
# num1 = 10
# num2 = 3
# operator = input()
#
# result = eval(f"{num1} {operator} {num2}")
# print(f'{num1} {operator} {num2} = {result}')
