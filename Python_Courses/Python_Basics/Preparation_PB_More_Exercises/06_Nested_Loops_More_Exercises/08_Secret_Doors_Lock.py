primes_between_2_and_6 = (2, 3, 5, 7)

first_digit_upper_boundary = int(input())
second_digit_upper_boundary = int(input())
third_digit_upper_boundary = int(input())

possible_passwords = []
for first in range(2, first_digit_upper_boundary + 1, 2):
    for second in primes_between_2_and_6:
        if second > second_digit_upper_boundary:
            break
        for third in range(2, third_digit_upper_boundary + 1, 2):
            current_password = f"{first} {second} {third}"
            possible_passwords.append(current_password)

print("\n".join(possible_passwords))
