start = int(input())
end = int(input())
magic_number = int(input())

comb_number = 0
n1 = 1
n2 = 1

should_break = False
for n1 in range(start, end + 1):
    for n2 in range(start, end + 1):
        comb_number += 1

        if n1 + n2 == magic_number:
            should_break = True
            break

    if should_break:
        break

if should_break:
    print(f'Combination N:{comb_number} ({n1} + {n2} = {magic_number})')
else:
    print(f'{comb_number} combinations - neither equals {magic_number}')
