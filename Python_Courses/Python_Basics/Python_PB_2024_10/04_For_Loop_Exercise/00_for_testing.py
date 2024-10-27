# print('it is all good')

# import time
#
# for i in range(0, 5, 1):  # [0, 1, 2, 3, 4]
#     time.sleep(1)
#     print(f' --> entering the iteration No - {i}')
#     print(type(i))
#     time.sleep(1)
#     print('command 2')
#     time.sleep(1)
#
# print('outside for loop')
# print(f'i = {i}')

# # 1.  stop  4 - 0 == 4
# for i in range(4):  # [0, 1, 2, 3]
#     print(f'current value of i is {i}!')

# # 2. start & stop
# for i in range(2, 6):  # [2, 3, 4, 5]  => 4; 6 - 2 == 4
#     print(i)

# # 3. start, stop, step
# for i in range(1, 25, 3):  # [start; stop) == [start; stop - 1]
#     print(i)

# for i in range(2, 4.5, 2.3):  # TypeError: 'float' object cannot be interpreted as an integer
#     print(i)

# # range(1, 10, 3) => [1, 1+3 == 4, 4+3 == 7] => [1, 4, 7]
# for num in range(1, 10, 3):
#     print(num)

# # range(1, 10, 77) => [1]
# for num in range(1, 10, 77):
#     print(num)

# # range(100, 10, 5) => []
# for num in range(100, 10, -5):
#     print(num)
# print(num)
# range(10, 29, -5) => []
# range(39, 29, -5) => [39, 34]

# import time
#
# for attempt in range(1, 6):  # [1, 2, 3, 4, 5]
#     print(f'Current attempt: {attempt}')
#     time.sleep(1)
#     print('-- Trying to connect to database...')
#     time.sleep(1)
#     if attempt == 2:
#         continue
#
#     print('-- NEXT COMMAND (TO BE SKIPPED ON ITERATION 2)')
#     time.sleep(1)
#
# print('outside for cycle')
# print(attempt)

# for _ in range(5):  # [0, 1, 2, 3, 4]  # _
#     print('command 1')
#     print('command 2')

# for i in range(10):  # [0, 1, 2, 3... 9]
#     print('action!')
#     print(f'i * 2 = {i * 2}')
#     print(i)
#     i += 10
#     print(i)

# help(range)
# continue

# print()

# text = "I am feeling good"  # type str
#
# print(len(text))  # 17
#
# print(text[2])  # "a"

# name = 'Simo'
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])

# for i in range(3):  # [0, 1, 2]
#     print(i)

# for ch in 'Simo':  # ['S', 'i', 'm', 'o']
#     print(ch)

# # string = '123456789'
# string = 'I am happy to learn how to code'
#
# # print(string[1])
#
# for i in range(0, len(string), 3):  # len(string) == 9; for i in range(9):  [0, 1, 2,... 8]
#     # print(i)
#     print(string[i])  # '1'; '4'; '7'
# import math
#
# print(10/3)
# print(int(10/3))
# print(math.floor(10/3))

# while True:
#     print('inf loop')

# for i in range(4):
#     name = input()
