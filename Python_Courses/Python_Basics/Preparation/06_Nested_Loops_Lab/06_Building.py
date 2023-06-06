floors = int(input())
rooms = int(input())

for i in range(floors, 0, -1):
    for j in range(rooms):
        if i == floors:
            print(f"L{i}{j} ", end="")
        elif i % 2 == 0:
            print(f"O{i}{j} ", end="")
        elif not i % 2 == 0:  # else:
            print(f"A{i}{j} ", end="")
    print()
