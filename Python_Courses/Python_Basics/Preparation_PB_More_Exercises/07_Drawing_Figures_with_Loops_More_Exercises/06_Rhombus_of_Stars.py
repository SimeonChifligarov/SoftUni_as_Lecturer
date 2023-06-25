rhombus_size = int(input())

for r in range(1, rhombus_size):
    print(f"{' ' * (rhombus_size - r)}*{' *' * (r - 1)}")
for r in range(1, rhombus_size + 1):
    print(f"{' ' * (r - 1)}*{' *' * (rhombus_size - r)}")
