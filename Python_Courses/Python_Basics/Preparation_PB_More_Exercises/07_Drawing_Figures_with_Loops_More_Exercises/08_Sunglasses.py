result = []

sunglasses_size = int(input())

top_row = f"{'*' * (2 * sunglasses_size)}{' ' * sunglasses_size}{'*' * (2 * sunglasses_size)}"
result.append(top_row)

for r in range(sunglasses_size - 2):
    if r == (sunglasses_size - 1) // 2 - 1:
        row = f"*{'/' * (2 * (sunglasses_size - 1))}*{'|'* sunglasses_size}*{'/' * (2 * (sunglasses_size - 1))}*"
    else:
        row = f"*{'/' * (2 * (sunglasses_size - 1))}*{' '* sunglasses_size}*{'/' * (2 * (sunglasses_size - 1))}*"
    result.append(row)

bottom_row = top_row
result.append(bottom_row)

print('\n'.join(result))
