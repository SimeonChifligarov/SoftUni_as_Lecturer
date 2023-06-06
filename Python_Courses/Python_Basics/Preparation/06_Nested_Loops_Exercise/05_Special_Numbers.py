number = int(input())

for num in range(1_111, 10_000):

    is_special = True
    num_as_string = str(num)
    for idx, digit in enumerate(num_as_string):
        if int(digit) == 0:
            is_special = False
            break

        if not number % int(digit) == 0:
            is_special = False
            break

    if is_special:
        print(num, end=" ")
