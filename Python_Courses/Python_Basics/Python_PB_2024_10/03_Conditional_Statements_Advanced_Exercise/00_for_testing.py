# print('it\'s advanced')

# number = 75
#
# if number > 50:
#     print('number is greater than 50')
#     if number > 80:
#         print('number is greater than 80')

# condition_1 -> value; simple check;
# 			-> complex check;

# 1. value check
# number = 0
#
# print(bool(number))
#
# if number:
#     print('number is not zero')

# name = ''
# print(bool(name))
#
# if name:
#     print('name is not an empty string')

# # 2. simple check
#
# number = 10
#
# print(number > 0)
#
# if number > 0:
#     print('number is positive')

# 3. complex check => and, or, not

# number = 100
#
# if number > 25 and number % 2 == 0:
#     print('number is greater than 25 and is even')

# print(4 + 5 * 2)  # 14
# print(4 + (5 * 2))  # 14
# print((4 + 5) * 2)  # 18

# priority => PNAO -> (), not, and, or

# print(True or False and False)     # and has precedence
# print((True or False) and False)   # parentheses change precedence
#
# print(not False or True)        # not has precedence
# print(not (False or True))      # parentheses change precedence

# name = 'Simo'
#
# if name == 'Petar' or name == 'Georgi':
#     print('name is Petar or Georgi')

# input_value = input()
# if input_value:
#     print('нещо си')
# else:
#     print('please insert non empty string')
#
# print(bool('Simo'))
# print(bool(''))

# number = 100
# text = 'hero'
#
# if 0 < number < 10_000:
#     print('number is between 0 and 10,000')
#     if text == 'hero':
#         ...

# str1 = '    '
# str2 = '\t'
#
# print(str1 == str2)
# print(f'{str1}!!!')
# print(f'{str2}!!!')

# number1 = 10_000_000
#
# number2 = 10000000
# print(number1 == number2)
# print(type(number1))
# print(number1)

# name = "10_0000"
#
# var = 'Simo'
# print(var)
#
# var = 3.14
# print(var)
#
# NUMBER = 13.37
#
# print(NUMBER)
# print(type(NUMBER))
#
# NUMBER = 'Simo'
# print(NUMBER)
# print(type(NUMBER))

# import this

# print(10 / 0)
