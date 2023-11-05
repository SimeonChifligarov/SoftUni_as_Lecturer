# •	Първи ред – четирицифрено число – началото на обхвата. Цяло число в интервала [1000…9999]
# •	Втори ред – четирицифрено число – края на обхвата. Цяло число в интервала [1000…9999]

first_number = int(input())
second_number = int(input())

first_number_as_string = str(first_number)
f_n_first = first_number_as_string[0]
f_n_second = first_number_as_string[1]
f_n_third = first_number_as_string[2]
f_n_forth = first_number_as_string[3]

second_number_as_string = str(second_number)
s_n_first = second_number_as_string[0]
s_n_second = second_number_as_string[1]
s_n_third = second_number_as_string[2]
s_n_forth = second_number_as_string[3]

for first in range(int(f_n_first), int(s_n_first) + 1):
    for second in range(int(f_n_second), int(s_n_second) + 1):
        for third in range(int(f_n_third), int(s_n_third) + 1):
            for forth in range(int(f_n_forth), int(s_n_forth) + 1):
                if first % 2 != 0 and second % 2 != 0 and third % 2 != 0 and forth % 2 != 0:
                    print(f"{first}{second}{third}{forth} ", end="")
