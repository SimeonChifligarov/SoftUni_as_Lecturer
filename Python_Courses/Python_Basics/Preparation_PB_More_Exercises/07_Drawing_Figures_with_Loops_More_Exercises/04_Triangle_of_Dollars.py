TRIANGLE_SYMBOL = "$"
triangle_rows_count = int(input())

for i in range(1, triangle_rows_count + 1):
    row = " ".join([TRIANGLE_SYMBOL] * i)
    print(row)
