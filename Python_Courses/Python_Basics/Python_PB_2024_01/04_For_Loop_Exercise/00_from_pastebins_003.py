import sys

n = int(input())
max_num = -sys.maxsize
sum_numbers = 0
for i in range(n):
    num = int(input())
    sum_numbers += num
    if num > max_num:
        max_num = num

if max_num == sum_numbers - max_num:
    print('Yes')
    print(f'Sum = {sum_numbers // 2}')
else:
    print('No')
    sum_numbers = sum_numbers - max_num
    print(f'Diff = {abs(sum_numbers - max_num)}')