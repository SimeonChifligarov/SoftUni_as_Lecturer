def is_even(num):
    return num % 2 == 0


def is_prime(num):
    if num == 1:
        return False

    for divisor in range(2, num):
        if num % divisor == 0:
            return False

    return True


first_digit_boundary = int(input())
second_digit_boundary = int(input())
third_digit_boundary = int(input())

for first in range(1, first_digit_boundary + 1):
    for second in range(1, second_digit_boundary + 1):
        for third in range(1, third_digit_boundary + 1):
            if is_even(first) and is_prime(second) and is_even(third):
                print(f"{first} {second} {third}")
