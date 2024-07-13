first_num = int(input())
second_num = int(input())

f_n_as_str = str(first_num)
f1, f2, f3, f4 = int(f_n_as_str[0]), int(f_n_as_str[1]), int(f_n_as_str[2]), int(f_n_as_str[3])

s_n_as_str = str(second_num)
s1, s2, s3, s4 = int(s_n_as_str[0]), int(s_n_as_str[1]), int(s_n_as_str[2]), int(s_n_as_str[3])

for d1 in range(f1, s1 + 1):
    if d1 % 2 == 0:
        continue
    for d2 in range(f2, s2 + 1):
        if d2 % 2 == 0:
            continue
        for d3 in range(f3, s3 + 1):
            if d3 % 2 == 0:
                continue
            for d4 in range(f4, s4 + 1):
                if d4 % 2 == 0:
                    continue

                print(f'{d1}{d2}{d3}{d4}', end=' ')
