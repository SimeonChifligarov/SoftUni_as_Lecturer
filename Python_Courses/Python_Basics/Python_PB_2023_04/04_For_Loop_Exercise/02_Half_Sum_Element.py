import sys

max_num = -sys.maxsize
num_sum = 0

num_count = int(input())  # e.g. 7

for _ in range(num_count):  # [0, 1, 2, 3, 4, 5, 6]
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num

    num_sum += current_num

rest_sum = num_sum - max_num
if max_num == rest_sum:
    print(f"Yes\nSum = {max_num}")
else:
    diff = abs(max_num - rest_sum)
    print(f"No\nDiff = {diff}")
