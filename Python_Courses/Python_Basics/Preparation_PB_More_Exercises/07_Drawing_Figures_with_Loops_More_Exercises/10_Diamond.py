# needs reformatting

import math

result = []

diamond_size = int(input())

starting_stars = 2 if diamond_size % 2 == 0 else 1
first_row = f"{'-' * ((diamond_size - starting_stars + 1) // 2)}" \
      f"{'*' * starting_stars}" \
      f"{'-' * ((diamond_size - starting_stars + 1) // 2)}"
result.append(first_row)

left_idx = math.ceil(diamond_size / 2) - 2
right_idx = left_idx + 3 if diamond_size % 2 == 0 else left_idx + 2

upper_half = (diamond_size - 2) // 2
if not diamond_size % 2 == 0:
    upper_half += 1
for r in range(upper_half):
    row = ['-'] * diamond_size
    row[left_idx] = '*'
    row[right_idx] = '*'
    left_idx -= 1
    right_idx += 1
    row_str = ''.join(row)
    result.append(row_str)

left_idx += 1
right_idx -= 1
lower_half = upper_half - 1
for r in range(lower_half):
    row = ['-'] * diamond_size
    left_idx += 1
    right_idx -= 1
    row[left_idx] = '*'
    row[right_idx] = '*'
    row_str = ''.join(row)
    result.append(row_str)


last_row = first_row
result.append(last_row)

if diamond_size == 1:
    print('*')
elif diamond_size == 2:
    print('**')
else:
    print('\n'.join(result))
