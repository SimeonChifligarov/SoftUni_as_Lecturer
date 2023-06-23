REAL_PASSWORD_INDEX = 3

result = []
control_value = int(input())

for a in range(1, 10):
    for b in range(1, 10):
        if a >= b:
            continue
        for c in range(1, 10):
            for d in range(1, 10):
                if c <= d:
                    continue

                if a * b + c * d == control_value:
                    result.append(1000 * a + 100 * b + 10 * c + 1 * d)

if result:
    print(" ".join([str(el) for el in result]))

if len(result) < 4:
    print("No!")
else:
    print(f"Password: {result[REAL_PASSWORD_INDEX]}")
