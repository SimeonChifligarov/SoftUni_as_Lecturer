# Solution 1
# диапазона от 1 до 1000,
# counter = 0
# for number in range(1, 1001):  # [1, 2, ... 1001) == [1, 2, ... 1000]
#     counter += 1
#     print(f'current operation no {counter}')
#     # които завършват на 7.
#     if number % 10 == 7:  # 23 % 10 == 3
#         print(number)

# # Solution 2
# counter = 0
# for number in range(7, 1001, 10):  # [7, 17, 27, ... 997]
#     counter += 1
#     print(f'current operation no {counter}')
#     print(number)

for number in range(7, 1001, 10):  # [7, 17, 27, ... 997]
    print(number)
