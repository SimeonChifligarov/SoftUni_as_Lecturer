# чете от конзолата цели числа,
# докато не се получи команда "stop".
prime_numbers_sum = 0
nonprime_numbers_sum = 0

while True:
    command = input()  # 'stop', OR number_as_str, e.g. '9'

    if command == 'stop':
        break

    number = int(command)

    if number < 0:
        print('Number is negative.')
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


print(f'Sum of all prime numbers is: {prime_numbers_sum}')
print(f'Sum of all non prime numbers is: {nonprime_numbers_sum}')
