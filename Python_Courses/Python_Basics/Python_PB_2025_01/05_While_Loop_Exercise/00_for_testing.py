# print('it workz ;)')


# condition                    # initialization 1.
# while condition:             # check          2.
#    some_logic_here...
#    change condition          # potential change 3.

# number = 13  # 1. init
# while number < 100:  # 2. check
#     print(number)
#
#     number += 10  # potential change 3.

# number = 13
# while number < 100:
#     if number == 43 or number == 53:
#         number += 10
#         continue
#
#     print(number)
#
#     number += 10

# number = 10000000000_0_000_000_000
# print(number)
# print(type(number))

# num_1 = 0.1
# num_2 = 0.2
#
# num_3 = num_1 + num_2
# print(num_3)
# print(num_3 == 0.3)

# print(0.1 + 0.2)
# print(0.2 + 0.2)
# print(0.3 + 0.2)

# help(range)

# for i in range(4, 10, 2):
#     print(i)

# for i in range(5):  # range(0, 5, 1) => [0, 5) == [0, 4] == [0, 1, 2, 3, 4]
#     print(i)
# print('trying to connect to database...')


# for i in range(1, 10):  # 10 - 1 == 9
#     print(i)

# for i in range(1, 25, 3):  # [1, 4, 7, ..., 22] == [1; )
#     print(i)

# range(1, 10, 3) => [1, 1+3 == 4, 4+3 == 7] => [1, 4, 7]
# range(1, 10, 77) => [1]
# range(100, 10, 5) => []
# range(10, 29, -5) => []
# range(39, 29, -5) => [39, 34]

# print(list(range(39, 29, -5)))
# print( list ( range(1, 10, 3) ) )

# for i in range(100, 10, 5):
#     print('here')

result_1 = '3:1'
result_2 = '5:2'

r_1_h = result_1[0]  # '3'
r_1_a = result_1[2]  # '1'
print(r_1_h)
print(r_1_a)
