n = int(input())

result = ''

for current_num in range(1_111, 10_000):

    current_number_as_str = str(current_num)

    is_special = True
    for d in current_number_as_str:
        digit = int(d)  # e.g. int('2') == 2

        if digit == 0:
            is_special = False
            break

        if n % digit != 0:
            is_special = False
            break

    if is_special:
        result += f'{current_num} '


print(result)
