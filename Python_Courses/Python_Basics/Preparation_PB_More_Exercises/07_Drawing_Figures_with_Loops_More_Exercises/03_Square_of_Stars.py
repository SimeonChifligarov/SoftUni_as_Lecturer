SQUARE_SYMBOL = "*"
square_side = int(input())

# [print(square_side * f"{SQUARE_SYMBOL} ") for _ in range(square_side)]
[print(" ".join([SQUARE_SYMBOL] * square_side)) for _ in range(square_side)]
