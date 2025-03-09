# print('it\'s working')

# # 1. var_name, var_type, var_value
# var = 'Simo'
#
# print(var)
#
# var = 13.37
#
# print(var)

# var1 = 'Simo'
# var2 = 12
#
# print(var1 + var2)

# var = 'S'
# print(type(var))  # <class 'str'>

# currency_type = input("What is the currency type? (usd/eur) ")  # 'usd', 'eur'
# currency = float(input("What is the amount? "))
#
# if currency_type == 'usd':
#     bgn = currency * 1.80
#     print(f'IN BGN: {bgn}')
# elif currency_type == 'eur':
#     bgn = currency * 1.95
#     print(f'IN BGN: {bgn}')

# 1. assignment
# num1 = 100

# print(num1)
# print(type(num1))

# 2. cast
# num2_as_string = '200'
# num2 = int(num2_as_string)
#
# print(num2)
# print(type(num2))

# # 3. run-time evaluation
# num3 = 100 + 20
#
# print(num3)
# print(type(num3))

# 1. assignment
# is_valid = True
#
# print(is_valid)  # True
# print(type(is_valid))  # <class 'bool'>

# 2. using bool()
# name = 'Simo'
# name = ''  # name = ""
# is_not_empty = bool(name)
#
# print(is_not_empty)  # True
# print(type(is_not_empty))  # <class 'bool'>

# # 3. run-time evaluation
# num = 1000
#
# is_greater_than_100 = num > 100
#
# print(is_greater_than_100)
# print(type(is_greater_than_100))

# is_valid = True  # keyword
# # True = 13
#
# true = 13.00

# num1 = 11
# num2 = 12
#
# print(num1 >= num2)  # 11 >= 12 == False

# print(1337)

# num = 1
#
# # is_greater_than_10 = num > 10  # 100 > 10 == True
#
# if num > 10:  # True
#     print('it is greater than 10')
#     print('inside if line 2')
#     print('inside if line 3')
#
# print('outside if line 4')

# num = -100
#
# if num > 10:  # True
#     print('it is greater than 10')
# elif num < 0:
#     print('it is less than 0')
# else:
#     print('it is not greater... :(')
#
# print('  -> outside if-elif-else')

# num = 1337
#
# if num > 100:
#     print('it is greater than 100')
# elif num > 200:
#     print('it is greater than 200')
# elif num > 300:
#     print('it is greater than 300')
# elif num > 400:
#     print('it is greater than 400')

# num = 1337
#
# print('case if-elif')
# if num > 100:
#     print('   it is greater than 100')
# elif num > 200:
#     print('   it is greater than 200')
#
# print('case if - if')
# if num > 100:
#     print('   it is greater than 100')
# if num > 200:
#     print('   it is greater than 200')

# num = 7
# print(f"{num:02d}")
# print(f"{num:.2f}")

# num = 1300
# result = num * 10 - 20
#
# print(f'{result}')

# num = 100
# print(num)
#
# # num = num + 10  # 110
# num += 10  # num = num + 10
# print(num)

# num = 1337
# print(f'Hard-coded part + templated part={num}')
# print('Hard-coded part + templated part={num}')

# a = int(input())
# b = int(input())
#
# result = abs(a - b)
# print(result)

# print(abs(-200))
# print(abs(200))
# import math


# num1 = 13.99
#
# # print(round(num1))  # 14
# print(math.ceil(num1))  # 14
# print(math.floor(num1))  # 13
#
# print(200 / 13)  # 15.384615384615385
# print(math.floor(200 / 13))  # ...
# print(200 // 13)  # ...

# import math

# print(math.ceil(13.37))


# from math import ceil, floor
#
# print(ceil(13.37))

# import this

# import antigravity
