number = int(input())

combinations = 0
for n1 in range(number + 1):
    for n2 in range(number + 1):
        for n3 in range(number + 1):
            if n1 + n2 + n3 == number:
                combinations += 1

print(combinations)
