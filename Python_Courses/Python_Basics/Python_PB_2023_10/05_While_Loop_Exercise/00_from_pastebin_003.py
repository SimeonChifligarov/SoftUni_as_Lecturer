# result = []

first_num = int(input())
second_num = int(input())

f_n_as_str = str(first_num)
f_f_digit = int(f_n_as_str[0])
f_s_digit = int(f_n_as_str[1])
f_t_digit = int(f_n_as_str[2])
f_fo_digit = int(f_n_as_str[3])

s_n_as_str = str(second_num)
s_f_digit = int(s_n_as_str[0])
s_s_digit = int(s_n_as_str[1])
s_t_digit = int(s_n_as_str[2])
s_fo_digit = int(s_n_as_str[3])

for f_digit in range(f_f_digit, s_f_digit + 1):
    if f_digit % 2 == 0:
        continue
    for s_digit in range(f_s_digit, s_s_digit + 1):
        if s_digit % 2 == 0:
            continue
        for t_digit in range(f_t_digit, s_t_digit + 1):
            if t_digit % 2 == 0:
                continue
            for fo_digit in range(f_fo_digit, s_fo_digit + 1):
                if fo_digit % 2 == 0:
                    continue
                # result.append(f_digit * 1_000 + s_digit * 100 + t_digit * 10 + fo_digit * 1)
                print(f_digit * 1_000 + s_digit * 100 + t_digit * 10 + fo_digit * 1, end=" ")

# print(*result, sep=" ")
