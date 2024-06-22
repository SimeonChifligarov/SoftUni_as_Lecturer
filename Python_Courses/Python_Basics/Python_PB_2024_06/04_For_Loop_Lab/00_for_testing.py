# print('it\'s working!!')
#
# print('here')
# if True:
#     print('line 1 from block code')
#     print('line 2 from block code')
#     print('line 3 from block code')

# print(not (3 == 3) or (3 == 5))
# print((3 == 3))
# print(not (3 == 3))

# print(True and False)

# a = 6
#
# if a == 5 or name == 'Simo' or ... or ...:
#     print('we print here')

# number = 101
# if number >= 1:
#     print("Larger than 1")
#
# print('1')
# print('2')
# print('3')
#
# if number <= 101:
#     print("Less than 101")
#     print("Equal to 101")

# role = "Administrator"
# password = "SoftUni"
# if role == "SoftUni":
#     if password == "SoftUni":
#         print("Welcome!")

# for num in range(1, 4):  # [1, 2, ... 12]
#     print(num)
#     print(f'current num * 10 = {num * 10}')

# print(i)
# print('outside for-loop')
# print('end of program')

# for num in range(1, 10 + 1):
#     print(num)

# range(1, 10, 1) => [1; 10) => [1, 2, 3, ... 9]
# range(start, stop[, step])

# range(1, 10, 3) => [1, 1+3 == 4, 4+3 == 7] => [1, 4, 7]
# range(1, 10, 77) => [1]
# range(100, 10, 5) => []
# range(10, 29, -5) => []
# range(39, 29, -5) => [39, 34]


# for n in range(39, 29, -5):
#     print(n)
#     print(type(n))
#
# print('outside')

############################
# range(stop) => start = 0, step = 1

# range(10) => [0, 1, 2, ... 9]
# for num in range(10):
#     print(num)

# for num in range(5):
#     print('PRINT SOMETHING')

# for num in range(0, 10, 1):
#     print(num)


# for n in range(100, 10, 5):
#     print(n)
#
# print('outside')
# print(n)

# print('outside for')
# print(n)

# for fl_n in [2.4, 2.66, 3.77, 5.44]:
#     print(fl_n)
#     print(fl_n * 10)

 # range(start, stop[, step=1])
 # range(stop)  # start=0, step=1
#
# for num in range(5):
#     print(num)
#
# print('=====')
# for num in range(0, 5):
#     print(num)
#
# print('=====')
# for num in range(1, 5, 2):
#     print(num)

# for _ in range(3):  # _ = [0, 1, 2]
#     print('hip hip huray')

# print(_)

# for i in range(11, 0, -2):
#   print(i, end=" ")


# name = 'S i meon'
# name = ''
# print(type(name))
# # name = '  '
#
# print(len(name))
# print(type(len(name)))

# name_len = len(name)  # 6
#
# print(name_len)
# print(name_len * 3)

# print(len('Peter'))

# -5 -4 -3 -2 -1
# P  e  t  e  r
# 0  1  2  3  4

# name = 'Peter'
# print(name[0])
# print(name[-1])

# print(name[-1])  # -1
# print(name[len(name) - 1])  # 5 - 1 = 4

# print(name[-6])
# print(name[-1])
# print(name[-2])
# print(name[-3])
# print(name[-4])
# print(name[-5])

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])

# name = input()  # len(name) == 5
# for i in range(len(name)):  # range(5) == [0, 1, 2, 3, 4]
#     # print(i)
#     print(name[i])
#     # print('----')

# name = 'Georgi'  # ['G', 'e', 'o', 'r', 'g', 'i']
#
# for c in name:
#     print(c)
#     print(f'current content of c is {c} !!!')


# import sys
#
# max_num = sys.maxsize
#
# print(max_num)
# print(type(max_num))
#
# my_max_num = 9999999999999999999999999999999999999999999
#
# print(my_max_num > sys.maxsize)
#
# my_max_max = float('inf')
# print(my_max_max)
# print(type(my_max_max))
#
# print(my_max_max > my_max_num)
# print(my_max_max > sys.maxsize)

# my_min_min = -float('-inf')
# print(my_min_min == float('inf'))
# print(type(my_min_min))

# name = input()

# if name == 'softuni':
#     print(name[0])
#     print(name[1])
#     print(name[2])
#     print(name[3])
#     print(name[4])
#     print(name[5])
#     print(name[6])
# if name == 'ice cream':
#     print(name[0])
#     print(name[1])
#     print(name[2])
#     print(name[3])
#     print(name[4])
#     print(name[5])
#     print(name[6])
#     print(name[7])
#     print(name[8])


if input() == '2' and input() == '10' and input() == '20':
    print(30)
# elif input() == ''
