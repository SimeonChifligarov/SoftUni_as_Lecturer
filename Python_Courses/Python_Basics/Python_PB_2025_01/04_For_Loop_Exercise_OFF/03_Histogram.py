p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

num_count = int(input())

for _ in range(num_count):
    current_number = int(input())

    if current_number < 200:
        p1_count += 1
    elif current_number < 400:
        p2_count += 1
    elif current_number < 600:
        p3_count += 1
    elif current_number < 800:
        p4_count += 1
    elif current_number >= 800:
        p5_count += 1

p1_percent = p1_count / num_count * 100
p2_percent = p2_count / num_count * 100
p3_percent = p3_count / num_count * 100
p4_percent = p4_count / num_count * 100
p5_percent = p5_count / num_count * 100

print(f"{p1_percent :.2f}%")
print(f"{p2_percent :.2f}%")
print(f"{p3_percent :.2f}%")
print(f"{p4_percent :.2f}%")
print(f"{p5_percent :.2f}%")
