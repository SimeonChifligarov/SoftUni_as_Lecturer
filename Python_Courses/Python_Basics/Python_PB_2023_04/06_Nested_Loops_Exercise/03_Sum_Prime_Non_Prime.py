sum_primes = 0
sum_non_primes = 0

command = input()  # "stop" OR number as string
while not command == "stop":
    current_number = int(command)

    if current_number < 0:
        print("Number is negative.")
        command = input()
        continue

    is_prime = True
    for num in range(2, current_number):
        if current_number % num == 0:
            is_prime = False
            break

    if is_prime:
        sum_primes += current_number
    else:
        sum_non_primes += current_number

    command = input()

print(f"Sum of all prime numbers is: {sum_primes}")
print(f"Sum of all non prime numbers is: {sum_non_primes}")
