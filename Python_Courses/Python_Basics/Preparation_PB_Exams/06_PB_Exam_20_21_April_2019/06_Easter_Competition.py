best_baker = ""
best_baker_points = 0

easter_breads = int(input())

for _ in range(easter_breads):
    baker = input()
    baker_points = 0
    command = input()
    while command != "Stop":
        points = int(command)
        baker_points += points
        command = input()

    print(f"{baker} has {baker_points} points.")
    if baker_points > best_baker_points:
        best_baker_points = baker_points
        best_baker = baker
        print(f"{baker} is the new number 1!")

print(f"{best_baker} won competition with {best_baker_points} points!")
