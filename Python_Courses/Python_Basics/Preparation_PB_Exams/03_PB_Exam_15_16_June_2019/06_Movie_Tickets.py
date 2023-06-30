a1 = int(input())  # in [65… 89]
a2 = int(input())  # in [66… 91]
n = int(input())  # in [1… 10]

for symbol_1 in range(a1, a2):
    if symbol_1 % 2 == 0:
        continue
    for symbol_2 in range(1, n):
        for symbol_3 in range(1, n // 2):
            if (symbol_1 + symbol_2 + symbol_3) % 2 != 0:
                print(f"{chr(symbol_1)}-{symbol_2}{symbol_3}{symbol_1}")
