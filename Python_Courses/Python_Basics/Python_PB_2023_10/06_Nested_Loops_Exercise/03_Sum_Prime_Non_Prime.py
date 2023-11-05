# която чете от конзолата цели числа, докато не се получи команда "stop".
prime_numbers_sum = 0
nonprime_numbers_sum = 0

command = input()  # "stop" OR integer as string, e.g. "3", "9"
while command != "stop":
    number = int(command)  # e.g. 3, 9
    if number < 0:
        print("Number is negative.")
        command = input()
        continue

    is_prime = True
    for n in range(2, number):
        if number % n == 0:
            is_prime = False
            break

    if is_prime:
        prime_numbers_sum += number
    else:
        nonprime_numbers_sum += number

    command = input()

print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {nonprime_numbers_sum}")
