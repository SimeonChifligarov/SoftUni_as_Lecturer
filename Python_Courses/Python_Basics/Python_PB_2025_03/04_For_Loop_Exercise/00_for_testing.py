# print('it is working')

# some_text = 'Simeon'
#
# for ch in some_text:  # ['S', 'i', 'm', 'e', 'o', 'n']
#     print(f'current char is {ch}')
#     print('command 1')
#     print('command 2')
#
# if
# in

# for num in range(10):  # [0, 1, 2... ]
#     print(num * 100)
#     print('line 1')

# for num in range(0, 5, 1):  # [0, 5) == [0, 4] => [0, 1, 2, 3, 4]
#     print(num)
#
# print('outside for-loop')

# for n in range(10_000):
#     print(n)
#     print('line 1')

# import time
#
# for i in range(5):
#     print(f'Attempt No: {i}')
#     time.sleep(1)
#     print('Trying to connect to database...')
#     time.sleep(1)

# 1.
# for i in range(6):  # [0, 6) == [0, 5] => [0, 1, 2, 3, 4, 5]
#     print(i)

# 2.
# for i in range(4, 9):  # [4, 9) == [4, 8] => [4, 5, 6, 7, 8]
#     print(i)

# 3.
# for i in range(1, 25, 3):
#     print(i)

# range



# range(1, 10, 3) => [1, 1+3 == 4, 4+3 == 7] => [1, 4, 7]

# for i in range(1, 10, 3):
#     print(i)
# range(1, 10, 77) => [1]
# for i in range(1, 10, 77):  # [1]
#     print(i)

# # range(100, 10, 5) => []
# for i in range(100, 10, 5):
#     print(i)

# # range(10, 29, -5) => []
# # range(39, 29, -5) => [39, 34]  34+(-5) == 34 - 5 == 29
# for i in range(39, 29, -5):
#     print(i)

# for i in range(4, 5.5, 2.5):  # TypeError: 'float' object cannot be interpreted as an integer
#     print(i)

# range(1, 10, 3) => [1, 1+3 == 4, 4+3 == 7] => [1, 4, 7]
# print(list(range(1, 10, 3)))
# print(list(range(100, 10, 5)))
# print(list(range(39, 29, -5)))

# range(1, 10, 77) => [1]
# range(100, 10, 5) => []
# range(10, 29, -5) => []
# range(39, 29, -5) => [39, 34]

# text = "I am feeling good"  # type str
#
# print(len(text))  # 17
#
# print(text[2])  # "a"

# name = 'Simo'  # ['S', 'i', 'm', 'o']
#
# # for i in range(len(name)):  # range(4) => [0, 1, 2, 3]
# #     print(name[i])
#
# second_char = name[1]  # we start counting from 0
# print(second_char)

# for i in range (1, 100, 100) пърият елемент е 1,
# после се опитва да прави нещо,  => start + step
# не става, излиза, връща само един елемент.

# for i in range(1, 100, 100):  # [1,]  Not 1 + 100 == 101;
#     print(i)

# for i in range(100, 10):  # 100, 100 + 1 == 101

# break
#
# import time
#
#
# for attempt in range(1, 6):  # [1, 2, 3, 4, 5]
#     print(f'Current attempt No: {attempt}!')
#     time.sleep(1)
#     print('-- Trying to connect to database...')
#     time.sleep(1)
#
#     # if attempt == 3:
#     #     print('-- -- Success!!!')
#     #     break
#
#     if attempt == 2:
#         continue
#
#     print('-- Command Line 2 (Will skip on iteration 2)')

# import sys
#
# print(f'{sys.maxsize:,}')  # 9223372036854775807
# print(type(sys.maxsize))  # <class 'int'>


# import math
#
# math.inf


# for num in range(3, 9):  # [3, 4, 5, 6, 7, 8]  => count 6 == stop-start == 9-3 == 6
#     print(num)

for num in range(6):  # stop-start == 6-0 == 6 ; [0, 1, 2, 3, 4, 5]
    print(num)
