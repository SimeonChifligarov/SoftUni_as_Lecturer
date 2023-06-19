MULTIPLIER = 2

num = float(input())
while num >= 0:
    result = num * MULTIPLIER
    print(f"Result: {result :.2f}")
    num = float(input())

print("Negative number!")
