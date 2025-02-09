prime_numbers_sum = 0
nonprime_numbers_sum = 0

command = input()  # 'stop' or int as a str, e.g. '3'
while command != 'stop':
    number = int(command)  # e.g. int('3') == 3

    if number < 0:
        print('Number is negative.')
        command = input()
        continue

    is_prime = True
    for divisor in range(2, number):  # [2, 3, 4, 5, 6]
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        prime_numbers_sum += number
    else:
        nonprime_numbers_sum += number

    command = input()

print(f'Sum of all prime numbers is: {prime_numbers_sum}')
print(f'Sum of all non prime numbers is: {nonprime_numbers_sum}')
