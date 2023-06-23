def is_prime(num):
    if num == 1:
        return False

    for divisor in range(2, num):
        if num % divisor == 0:
            return False

    return True


potential_results = []
results = []

starting_for_first_pair = int(input())
starting_for_second_pair = int(input())
ending_for_first_pair = int(input())
ending_for_second_pair = int(input())

for f in range(starting_for_first_pair, starting_for_first_pair + ending_for_first_pair + 1):
    for s in range(starting_for_second_pair, starting_for_second_pair + ending_for_second_pair + 1):
        current_number = f * 100 + s
        # print(current_number)
        potential_results.append(current_number)


for num in potential_results:
    first_part = num // 100
    second_part = num % 100
    if is_prime(first_part) and is_prime(second_part):
        results.append(num)

print(*results, sep="\n")
