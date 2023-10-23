# print('it is all right ;)')

# for number in range(1, 25, 3):  # [2, 3]  == [2; 4)
#     print(number)
#     # print(type(number))
#     # print('we are here!')
#
# print('---')
# print('after the for-cycle')

# num = int(input())
#
# if num > 10:
#     my_var = 1337
# else:
#     my_var = 100
#
# print(my_var)

# PyCharm -> IDE

# help(range)
# range()

# text = "I am feeling good"
#
# print(len(text))  # 17
#
# print(text[2])  # "a"

# for attempt in range(1, 6):  # [1, 2, 3, 4, 5]
#     print(f"Attempt No {attempt}")
#     print("Trying to connect to DB...")
#     if attempt == 3:
#         print("Success!!!")
#         break

# print("final value")
# print(attempt)
# for _ in range(5):  # [0, 1, 2, 3, 4]
#     print("Trying to connect to DB...")

# for i in range(1, 25, 3):
#     print(i)
#     if i == 10:
#         print('here')
#         continue
#
#     print("after IF, but inside FOR")

# for i in range(10):  # [0, 1, 2..., 9]
#     if 3 <= i < 5:
#         print('between 3 & 5')
#         continue
#
#     print('core logic here line 1')
#     print('core logic here line 2')

# number = 2 / 3  # 0.6666666666666666666666666
#
# print(f"{number :.2%}")

# is_break = False
# for i in range(15):
#     print(i)
#     if i == 10:
#         print('exit with break')
#         is_break = True
#         break
# else:
#     print("WAS ENDED WITHOUT BREAK")
#
# if is_break:
#     print("was broken")
# else:
#     print("was NOT broker")
# ...

# number = int(input())
#
# if number > 100:
#     print('more than 100')
# elif number > 10:
#     print('more than 10')
# else:
#     print('something else')
# import math
# import sys
#
# number = 13.333337
#
# print(math.ceil(number))
# print(math.floor(number))

# help(sys.maxsize)

# my_name = "Simo"  # = input()
#
# print(my_name[0])
# print(my_name[1])
# print(my_name[2])
# print(my_name[3])
# print('------')
# print("abcdef"[2])

# print("Sept" == "Sept ")

text = "Hello Bulgaria!😍"

# for i in range(len(text)):
#     print(f"index {i}: character: {text[i]}")

for idx, char in enumerate(text):
    print(f"index {idx}: char: {char}")

