# # print('it workzzz')
#
# first_name = input()  # ["Peter", "Светлин", "Maria", "Geek"]
# last_name = ["Nikolov", "Наков", "Ivanova", "Coder"]
# age = [22, 29, 19, 15]
# town = ["Varna", "Велико Търново", "Pleven", "Codeland"]
#
# for i in range(len(first_name)):
#     text = f"You are {first_name[3]} {last_name[3]}, a {age[3]}-years old person from {town[3]}."
#     print(text)

# # # print('it works!')
# #
# #
# # # # pseudo-code
# # # if is_rainy:
# # #     take_umbrella()
# # # else:
# # #     ...
# #
# # # user_input = ...
# # # UserInput = ...
# # # userInput = ...
# # # # user-input = ...
# #
# # # age = 23
# # # Age = 24
# # # AGE = 33
# # #
# # # print(age)
# # # age = 200
# #
# # # name = 'Simeon'
# # name = "Simeon Кирилица 😎✅"
# #
# # print(name)
# # print(type(name))  # <class 'str'>
# #
# # age = 23
# #
# # print(age)
# # print(type(age))  # <class 'int'>
# #
# # weight = 65.5
# #
# # print(weight)
# # print(type(weight))  # <class 'float'>
#
# # # name = 'Simo'
# # name = input()
# # age = int(input())  # int('22') == 22
# #
# # print(type(age))
# #
# # print(f'Hello, {name}, {age} years old!')
#
# # print(3 + 2 * 10)
# # print((3 + 2) * 10)
#
# # print('Simeon's pet')
# # print('Simeon\'s pet')
# # print("Simeon's pet")
#
# # name1 = 'Gosho1'
# # name2 = "Gosho"
# # print(type(name1))
# # print(type(name2))
# # print(name1 == name2)
#
# # name = 'gosho'  # ...
#
# # age = int(input())  # int('22') == 22
# #
# # print(f'next age is {age + 1}')
#
# # name = str(input())  # str('33a') == '33a'
#
# # print('Hello SoftUni')
# # Ctrl+Alt+L
#
# # age = int(input())
#
# # total_cost = 1000
# # discount = 15 / 100  # 0.15
# #
# # total_cost_after_discount = total_cost - (total_cost * discount)
# # print(total_cost_after_discount)
# #
# # print(total_cost * (1 - discount))
#
# # age = int(input('Въведете възрастта си моля: '))
# import math
#
# number = 33.65
# number_rounded = round(number)  # 34
# number_floor = math.floor(number)  # 33
# number_ceil = math.ceil(number)  # 34
#
# print(number_rounded)
# print(number_floor)
# print(number_ceil)
#
# # num_1 = 24
# # num_2 = 5
# #
# # print(num_1 / num_2)
# # print(num_1 // num_2)
# # print(num_1 % num_2)
#
# Вход
length = int(input())  # дължина в см
width = int(input())  # широчина в см
height = int(input())  # височина в см
percentage = float(input())  # процент зает от аквариума

# Пресмятане на обема на аквариума в кубични сантиметри
volume_in_cm3 = length * width * height

# Преобразуваме кубичните сантиметри в кубични дециметри (литри)
volume_in_liters = volume_in_cm3 / 1000

# Намаляваме заетия процент
water_needed = volume_in_liters * (1 - percentage / 100)

# Изход
print(f"{water_needed:.2f}")
