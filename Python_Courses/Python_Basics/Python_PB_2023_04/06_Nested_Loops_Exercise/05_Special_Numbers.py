number = int(input())

for num in range(1_111, 10_000):  # num holds each of [1111, 1112, ..., 9999]

    is_special = True
    num_as_str = str(num)  # num_as_str "1111"
    for _, digit in enumerate(num_as_str):  # digit holds each of ["1", "1", "1", "1"]
        current_digit = int(digit)

        if current_digit == 0:
            is_special = False
            break

        if not number % current_digit == 0:
            is_special = False
            break

    if is_special:
        print(f"{num}", end=" ")
