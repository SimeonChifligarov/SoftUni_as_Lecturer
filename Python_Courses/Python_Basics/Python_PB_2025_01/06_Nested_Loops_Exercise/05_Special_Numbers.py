# import time
result = ''
input_number = int(input())

# for num in range(1_111, 9_999 + 1):
for num in range(1_111, 10_000):  # ... 1120

    number_as_str = str(num)  # '2418'

    is_special = True
    for d in number_as_str:  # ['2', '4', '1', '8']
        d_as_int = int(d)  # int('2') == 2

        if d_as_int == 0:
            is_special = False
            break

        if input_number % d_as_int != 0:
            is_special = False
            break

    if is_special:
        result += f'{num} '
        # print(num, end=' ')
        # time.sleep(1)

print(result)
