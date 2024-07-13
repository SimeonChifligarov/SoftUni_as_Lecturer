range_start = int(input())  # 4-digit number
range_end = int(input())  # 4-digit number

range_start_as_str = str(range_start)
f1, f2, f3, f4 = int(range_start_as_str[0]), int(range_start_as_str[1]), int(range_start_as_str[2]), int(
    range_start_as_str[3])

range_end_as_str = str(range_end)
s1, s2, s3, s4 = int(range_end_as_str[0]), int(range_end_as_str[1]), int(range_end_as_str[2]), int(range_end_as_str[3])

for n1 in range(f1, s1 + 1):
    if n1 % 2 == 0:
        continue
    for n2 in range(f2, s2 + 1):
        if n2 % 2 == 0:
            continue
        for n3 in range(f3, s3 + 1):
            if n3 % 2 == 0:
                continue
            for n4 in range(f4, s4 + 1):
                if n4 % 2 == 0:
                    continue

                print(f'{n1}{n2}{n3}{n4}', end=' ')
