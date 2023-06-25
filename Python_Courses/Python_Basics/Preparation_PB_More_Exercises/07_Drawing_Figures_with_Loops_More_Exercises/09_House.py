result = []

house_size = int(input())

roof_size = (house_size + 1) // 2

starting_stars = 2 if house_size % 2 == 0 else 1
for r in range(roof_size):
    row = f"{'-' * ((house_size - starting_stars) // 2)}{'*' * starting_stars}{'-' * ((house_size - starting_stars) // 2)}"
    result.append(row)
    starting_stars += 2

base_size = house_size - roof_size
for r in range(base_size):
    row = f"|{'*' * (house_size - 2)}|"
    result.append(row)

print('\n'.join(result))
