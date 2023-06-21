numbers_count = int(input())
total_sum = 0
for _ in range(numbers_count):
    total_sum += int(input())

print(f"{total_sum / numbers_count :.2f}")
