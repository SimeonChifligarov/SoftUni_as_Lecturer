counts = {
    "red": 0,
    "orange": 0,
    "blue": 0,
    "green": 0,
}

eggs_count = int(input())

for _ in range(eggs_count):
    egg_color = input()  # "red", "orange", "blue", "green"
    counts[egg_color] += 1

max_count = 0
max_color = ""
for color, count in counts.items():
    print(f"{color.capitalize()} eggs: {count}")
    if count > max_count:
        max_count = count
        max_color = color

print(f"Max eggs: {max_count} -> {max_color}")
