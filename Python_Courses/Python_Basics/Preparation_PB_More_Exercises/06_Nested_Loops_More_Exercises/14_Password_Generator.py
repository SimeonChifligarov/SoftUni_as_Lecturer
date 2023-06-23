result = []

n = int(input())
l = int(input())

for first in range(1, n + 1):
    for s in range(1, n + 1):
        for t in range(97, 97 + l):
            for f in range(97, 97 + l):
                for fifth in range(1, n + 1):
                    if fifth <= max(first, s):
                        continue

                    current_password = f"{first}{s}{chr(t)}{chr(f)}{fifth}"
                    result.append(current_password)

print(" ".join(result))
