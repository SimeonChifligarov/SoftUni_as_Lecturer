# # Solution 1
#
# number_of_couples = int(input())
# is_equal = True
# diff_as_list = []
# previous_sum = 0
# current_sum = 0
#
# for couple in range(1, number_of_couples+1):
#     num_one = int(input())
#     num_two = int(input())
#     current_sum = num_one + num_two
#     if couple == 1:
#         previous_sum = current_sum
#     if current_sum == previous_sum:
#         continue
#     else:
#         is_equal = False
#         diff = current_sum - previous_sum
#         diff_as_list.append(abs(diff))
#     previous_sum = current_sum
#
# if is_equal:
#     print(f'Yes, value={current_sum}')
# else:
#     print(f'No, maxdiff={max(diff_as_list)}')
#
#

# ##############################
# Solution 2

n = int(input())
current_sum = int(input()) + int(input())

diff_sum = 0

for _ in range(n - 1):
    next_sum = int(input()) + int(input())

    if abs(current_sum - next_sum) > diff_sum:
        diff_sum = abs(current_sum - next_sum)

    current_sum = next_sum

if diff_sum == 0:
    print(f"Yes, value={current_sum}")
else:
    print(f"No, maxdiff={diff_sum}")

