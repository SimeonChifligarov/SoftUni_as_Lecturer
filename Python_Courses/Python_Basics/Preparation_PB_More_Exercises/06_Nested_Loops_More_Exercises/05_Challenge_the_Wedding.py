possible_couples = []

males_count = int(input())
females_count = int(input())
max_tables_count = int(input())

for m in range(1, males_count + 1):
    for f in range(1, females_count + 1):
        possible_couple = f"({m} <-> {f})"
        possible_couples.append(possible_couple)

result = possible_couples[:max_tables_count]
print(*result, sep=" ")
