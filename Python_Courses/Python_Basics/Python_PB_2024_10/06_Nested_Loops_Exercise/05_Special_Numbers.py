number = int(input())

result_string = ''
for n in range(1111, 9999 + 1):  # [1111, 1112, ....]

    n_as_string = str(n)  # '1111'

    is_special = True
    for d in n_as_string:  # d -> ['1', '1', '1', '1']
        digit = int(d)

        if digit == 0:
            is_special = False
            break

        if number % digit != 0:
            is_special = False
            break

    if is_special:
        # print(f'{n} ', end='')
        result_string += f'{n} '

print(result_string)
