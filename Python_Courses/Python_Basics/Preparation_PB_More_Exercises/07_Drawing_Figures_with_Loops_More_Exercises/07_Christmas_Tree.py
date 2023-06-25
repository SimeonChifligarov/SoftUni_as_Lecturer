result = []

christmas_tree_size = int(input())

result.append(f"{' ' * christmas_tree_size} |")
for i in range(1, christmas_tree_size + 1):
    row = f"{' ' * (christmas_tree_size - i)}{'*' * i} | {'*' * i}{' ' * (christmas_tree_size - i)}"
    result.append(row)

print('\n'.join(result))
