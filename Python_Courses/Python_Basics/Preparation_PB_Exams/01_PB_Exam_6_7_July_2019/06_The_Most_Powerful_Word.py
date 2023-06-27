vowels = ('a', 'e', 'i', 'o', 'u', 'y')

words = []

command = input()
while command != "End of words":
    current_word = command
    points = 0
    for char in current_word:
        points += ord(char)

    if current_word[0].lower() in vowels:
        points *= len(current_word)
    else:
        points = int(points / len(current_word))

    word = {"word": current_word, "points": points}
    words.append(word)

    command = input()

# print(words)
words.sort(key=lambda w: -w['points'])
best_word = words[0]

print(f"The most powerful word is {best_word['word']} - {best_word['points']}")
