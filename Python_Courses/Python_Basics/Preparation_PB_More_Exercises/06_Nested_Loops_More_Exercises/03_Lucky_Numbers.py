possible_lucky_numbers = []
lucky_numbers = []

num = int(input())

for first in range(1, 10):
    for s in range(1, 10):
        for t in range(1, 10):
            for f in range(1, 10):
                if first + s == t + f:
                    possible_lucky_number = 1000 * first + 100 * s + 10 * t + 1 * f
                    possible_lucky_numbers.append(possible_lucky_number)

for p in possible_lucky_numbers:
    first_two_sum = p // 1000 + (p // 100) % 10
    if num % first_two_sum == 0:
        lucky_numbers.append(p)

print(' '.join([str(n) for n in lucky_numbers]))
