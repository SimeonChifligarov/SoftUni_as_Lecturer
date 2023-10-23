text = input()
points = 0
text_length = len(text)
for i in range(text_length):  # [0, 1, 2, ... 3]
    if text[i] == "a":  # 0 == "a"
        points += 1
    elif text[i] == "e":
        points += 2
    elif text[i] == "i":
        points += 3
    elif text[i] == "o":
        points += 4
    elif text[i] == "u":
        points += 5
print(points)
