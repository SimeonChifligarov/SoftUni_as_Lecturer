TRIANGLE_SYMBOL = "$"
triangle_symbols_count = int(input())

drawn_symbols_count_left = triangle_symbols_count
for i in range(1, triangle_symbols_count + 1):
    row_symbols = min(i, drawn_symbols_count_left) if drawn_symbols_count_left > 0 else i
    row = " ".join([TRIANGLE_SYMBOL] * row_symbols)
    print(row)

    drawn_symbols_count_left -= i
    if drawn_symbols_count_left < 0:
        break


