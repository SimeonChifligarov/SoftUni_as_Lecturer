p1_count = 0
p2_count = 0
p3_count = 0

numbers_count = int(input())

for _ in range(numbers_count):
    current_number = int(input())

    if current_number % 2 == 0:
        p1_count += 1

    if current_number % 3 == 0:
        p2_count += 1

    if current_number % 4 == 0:
        p3_count += 1

print(f"{p1_count / numbers_count :.2%}")
print(f"{p2_count / numbers_count :.2%}")
print(f"{p3_count / numbers_count :.2%}")
