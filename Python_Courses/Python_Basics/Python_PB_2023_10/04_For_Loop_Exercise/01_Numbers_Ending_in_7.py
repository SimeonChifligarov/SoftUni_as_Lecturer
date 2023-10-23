# # Solution 1
#
# counter = 0
# for num in range(1, 1001):  # [1, 2, 3, ... 1000] => count = 1000
#     counter += 1
#     print(f"Operation No {counter}")
#     if num % 10 == 7:
#         print(num)

# # Solution 2
#
# counter = 0
# for num in range(7, 1001, 10):  # [7, 17, ..., 997] => count = 100
#     counter += 1
#     print(f"Operation No: {counter}")
#     print(num)


# Solution real

# # Solution 1
#
# for num in range(1, 1001):
#     if num % 10 == 7:
#         print(num)

# Solution 2

for num in range(7, 1001, 10):
    print(num)
