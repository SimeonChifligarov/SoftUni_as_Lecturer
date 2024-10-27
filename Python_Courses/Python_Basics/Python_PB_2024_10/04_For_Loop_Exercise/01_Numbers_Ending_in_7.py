# диапазона от 1 до 1000, които завършват на 7.

# # 1.
# counter = 0
# for num in range(1, 1001):  # [1, 2, ..., 1001)  == [1, 2, ..., 1000]
#     counter += 1
#     print(f'Operation no: {counter}')
#     if num % 10 == 7:
#         print(num)

# # 2.
# counter = 0
# for num in range(7, 1001, 10):  # [7, 17, 27, 37, ... 997]
#     counter += 1
#     print(f'Operation no: {counter}')
#     print(num)

for num in range(7, 1001, 10):  # [7, 17, 27, 37, ... 997]
    print(num)
