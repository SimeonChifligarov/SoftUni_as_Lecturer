letters = []
result = []

first_letter = input()
last_letter = input()
skip_letter = input()

for letter in range(ord(first_letter), ord(last_letter) + 1):
    letters.append(chr(letter))

for first_letter in letters:
    for second_letter in letters:
        for third_letter in letters:
            if skip_letter in (first_letter, second_letter, third_letter):
                continue
            result.append(f"{first_letter}{second_letter}{third_letter}")

print(' '.join(result), len(result))
