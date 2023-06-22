possible_digits = []
result = []

start_digit = int(input())
end_digit = int(input())

for d in range(start_digit, end_digit + 1):
    possible_digits.append(d)

for first in possible_digits:
    for second in possible_digits:
        for third in possible_digits:
            for forth in possible_digits:
                if (first % 2 == 0 and forth % 2 == 0) or (first % 2 != 0 and forth % 2 != 0):
                    continue
                if first < forth:
                    continue
                if (second + third) % 2 != 0:
                    continue

                result.append(1000 * first + 100 * second + 10 * third + 1 * forth)

print(' '.join([str(n) for n in result]))
