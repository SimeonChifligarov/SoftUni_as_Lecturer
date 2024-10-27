# чете n-на брой цели числа, въведени от потребителя
import sys

numbers_count = int(input())  # int('7') == 7

total_sum = 0
biggest_num = -sys.maxsize

for _ in range(numbers_count):  # [0, 1, 2, 3... 6]
    current_number = int(input())

    total_sum += current_number
    if current_number > biggest_num:
        biggest_num = current_number

if biggest_num == total_sum - biggest_num:
    print('Yes')
    print(f'Sum = {biggest_num}')
else:
    diff = abs(biggest_num - (total_sum - biggest_num))
    print('No')
    print(f'Diff = {diff}')
