# print('it works!')

# name = input()
# while name != "End":
#     if name == 'Nakov':
#         print(f'Will skip with {name}')
#         name = input()
#         continue
#
#     print(f'Hello, {name}!')
#     name = input()

# import time


# for week in range(1, 5):
#     time.sleep(1)
#     print(f'Current week - {week}:')
#
#     for day in range(1, 8):
#         time.sleep(1)
#         print(f'--- Day - {day}')

# # 1
# counter = 0
# command = input()
# while command != "End":
#     counter += 1
#
#     if counter >= 3:
#         break
#     command = input()

# # 2
# counter = 0
# command = input()
# while counter < 3:
#     counter += 1
#
#     if command == "End":
#         break
#     command = input()

# # 3
# while command != 'End' and counter < 3 and ... or ...:
#     ...

# budget = 0
#
# while budget < 1000:
#     print(f'current budget {budget}')
#     for day in range(1, 8):
#         budget += 150
#
# print(f'I am going to vacation, because I earn {budget}')

# money_needed = 1000
# should_break = False
# budget = 0
# for day in range(1, 6):   # [1, 2, 3, 4, 5]
#     print(f"=> I am working day - {day}")
#     for hour in range(1, 9):  # [1, 2, 3, 4, 5, 6, 7, 8]
#         if hour == 5:
#             print(f"Hour {hour} - I am taking a break")
#             continue
#         print(f"--- I am working hour - {hour}; still day is {day}")
#         budget += 150
#
#         if budget >= 1000:
#             should_break = True
#             break
#
#     if should_break:
#         break
#
# print('---')
# print(budget)

# should_break = False
# for week in range(1, 5):
#     if week > 1:
#         print(day)
#     print(f'Current week - {week}:')
#
#     for day in range(1, 8):
#         print(f'--- Day - {day}', end="; ")
#         # if week == 3 and day == 2:
#         #     should_break = True
#         #     break
#
#     if should_break:
#         break
#     print()  # '', end='\n'

# print('line 1')
# print()
# print('line 2')

# import time
#
# for week in range(1, 5):
#     time.sleep(1)
#     print(f'Current week - {week}:')
#
#     for day in range(1, 8):
#         time.sleep(1)
#         print(f'--- Day - {day}; week - {week}')

# text = "I am here!"
# i = 0
# for ch in text:
#     print(f'${ch}$ - {i}')
#     i += 1

# for i in range(len(text)):
#     ch = text[i]
#     print(f'${ch}$ - {i}')

# for i, ch in enumerate(text):
#     print(f'${ch}$ - {i}')

# number = 5432

# number_as_string = str(number)  # '5432'
#
# for digit in number_as_string:
#     print(digit)
#     print(type(digit))

# for digit in number:
#     print(digit)

# number = 5432
# ll = []
# while number > 0:
#     digit = number % 10
#     # print(digit)
#     ll.append(digit)
#     number = number // 10
#
# print(*ll[::-1], sep='\n')


# text = 'Simo some'
#
# for i, ch in enumerate(text):
#     # print(something)
#     # print(type(something))
#     print(i, ch)

# number = 13
# # number = 8
# #
# is_prime = True
# for divisor in range(2, number):  # [2, 3, 4..., 12]
#     if number % divisor == 0:
#         is_prime = False
#         break
#
# print(f'current number {number} is primer = {is_prime}')

# print(8 % 2 == 0)
# print(8 % 3 == 0)
# print(8 % 4 == 0)
# print(8 % 5 == 0)
# print(8 % 6 == 0)
# print(8 % 7 == 0)

# print(13 % 11)

# n = 16
#
# current_number = 2419
# current_number_as_str = str(current_number)
#
# is_special = True
# for d in current_number_as_str:  # '2419'
#     digit = int(d)  # e.g. int('2') == 2
#
#     if n % digit != 0:
#         is_special = False
#         break
#
# print(f'current number - {current_number}; is special - {is_special}')

# print(16 % 2)
# print(16 % '2')

number = int(input())

max_digits = 10 ** (len(str(number)) - 1)

# print(max_digits)

while max_digits > 0:
    print(number // max_digits)
    number %= max_digits
    max_digits //= 10
