# print('test "if advanced"')

# number = 75
#
# if number > 50:
#     print('number is greater than 50')
#     if number > 80:
#         print('number is greater than 80')

# [pseudocode]
# condition_1 -> value; simple check;
# 			-> complex check;

# [1] -> value
# number = 0
# print(bool(number))
#
# if number:
#     print('number is different from 0')

# user_name = ''
# print(bool(user_name))
#
# if user_name:
#     print('username is not empty string')

# # [2] -> simple check
# number = 100
# if number > 50:
#     print('the number is greater than 50')


# # [3] -> complex check
#
# number = 100
# if 50 < number < 200:
#     print('number is between 50 and 200')

# number = 1000
#
# is_number_eq_100 = number == 100
# print(is_number_eq_100)

# print(5 + 3 * 2)  # 11
# print(5 + (3 * 2))  # 11
# print((5 + 3) * 2)  # 16

# number = 100
# if not number > 50:
#     print('number is not greater than 50')


# number = 75
#
# # [pythonic way of this complex check]
# if 50 < number < 80:
#     print('number is between 50 and 80')

# print(True or False and False)     # and has precedence
# print((True or False) and False)   # parentheses change precedence
#
# print(not False or True)        # not has precedence
# print(not (False or True))      # parentheses change precedence

# number = 10
#
# if number > 50 or username != "Gosho":
#     print('here')
# else:
#     print('false')

# a = 100
# b = 200
# diff = a + b ** 3 - 226 // 13
#
# print(f'Complex math formula return - {diff}')
#
# username = 'Simo'
#
# # complex_check = username == 'Gosho' or 'Pesho'
# # print(complex_check)
#
# if username == 'Gosho' or 'Pesho':
#     print('it is true')

# discount = 50 / 100
# extra_discount = 50 / 100
#
# price = 1000
# price_after_discount = price * (1 - discount)
# print(price_after_discount)
#
# price_after_extra_discount = price_after_discount * (1 - extra_discount)
# print(price_after_extra_discount)
#
# print('====')
# print(price * (1 - (discount + extra_discount)))

# import this

number = 100

# if number == 'Pesho':
#     print('will not print')
# else:
#     print('will print this one')

print('will not print') if number == 'Pesho' else print('will print this one')
