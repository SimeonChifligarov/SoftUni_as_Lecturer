# # Solution 1
# for num in range(1, 1001):
#     if num % 10 == 7:
#         print(num)

# Solution 2
ENDING_WITH = 7

for num in range(ENDING_WITH, 1001, 10):
    print(num)
