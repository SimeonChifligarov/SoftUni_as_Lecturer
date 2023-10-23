p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

numbers_count = int(input())

for _ in range(numbers_count):  # [0; numbers_count - 1] => count == numbers_count
    current_number = int(input())
    if current_number < 200:
        p1_count += 1  # p1_count = p1_count + 1
    elif current_number < 400:  # [200; 400) == [200; 399]
        p2_count += 1
    elif current_number < 600:
        p3_count += 1
    elif current_number < 800:
        p4_count += 1
    else:  # eq. elif current_number >= 800:
        p5_count += 1

# percent = target / total * 100
# total_count = p1_count + p2_count + p3_count + p4_count + p5_count

print(f"{p1_count / numbers_count :.2%}")
print(f"{p2_count / numbers_count :.2%}")
print(f"{p3_count / numbers_count :.2%}")
print(f"{p4_count / numbers_count :.2%}")
print(f"{p5_count / numbers_count :.2%}")
