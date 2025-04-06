number = int(input())

# 1. взимаме всяко число от 1_111 до 9_999
for num in range(1_111, 10_000):
    # 2. проверяваме дали числото е 'специално'

    is_special = True
    num_as_str = str(num)  # str(2418) == '2418'
    for d in num_as_str:  # ['2', '4', '1', '8']
        d_as_int = int(d)  # int('2') == 2

        if d_as_int == 0:
            is_special = False
            break

        if number % d_as_int != 0:
            is_special = False
            break
    #    -> ако е специално => печатим го на конзолата
    if is_special:
        print(num, end=' ')
