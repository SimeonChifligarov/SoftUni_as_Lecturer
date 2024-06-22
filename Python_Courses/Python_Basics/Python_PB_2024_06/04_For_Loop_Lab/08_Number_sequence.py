import sys

n = int(input())

min_num = sys.maxsize  # min_num = 99999999999999999999999999999999
max_num = -sys.maxsize  # max_num = -99999999999999999999999999999999

for _ in range(n):
    curr_number = int(input())
    # if _ == 0:
    #     min_num = curr_number
    #     max_num = curr_number

    if curr_number < min_num:
        min_num = curr_number

    if curr_number > max_num:
        max_num = curr_number

print(f'Max number: {max_num}')
print(f'Min number: {min_num}')
