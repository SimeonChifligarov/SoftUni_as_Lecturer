prime_numbers_sum = 0
nonprime_numbers_sum = 0

command = input()  # 'stop' OR number_as_string
while command != 'stop':
    current_number = int(command)

    if current_number < 0:
        print('Number is negative.')
        command = input()
        continue

    is_prime = True
    for divisor in range(2, current_number):  # [2, 3, 4..., 12]
        if current_number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        prime_numbers_sum += current_number
    else:
        nonprime_numbers_sum += current_number

    command = input()

print(f'Sum of all prime numbers is: {prime_numbers_sum}')
print(f'Sum of all non prime numbers is: {nonprime_numbers_sum}')
