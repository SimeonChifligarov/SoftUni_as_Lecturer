# диапазона от 1 до 1000, които завършват на 7.

# # Solution 1
# counter = 0
# for num in range(1, 1001):  # [1, 2, 3..., 1000]
#     # counter += 1
#     # print(f'Operation No {counter}')
#     if num % 10 == 7:
#         print(num)

# # Solution 2
# start_number = 7
# counter = 0
# for num in range(start_number, 1001, 10):  # [7, 17, 27, ... 997]
#     # counter += 1
#     # print(f'Operation No {counter}')
#     print(num)


# Solution 1
# counter = 0
# for num in range(1, 1001):  # [1, 2, 3..., 1000]
#     counter += 1
#     result = counter ** 9 * (3.14)
#     # print(f'Operation No {counter}')
#     if num % 10 == 7:
#         print(num)