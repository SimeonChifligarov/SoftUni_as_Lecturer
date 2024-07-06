import time

floors = int(input())
rooms = int(input())

for f in range(floors, 0, -1):
    for r in range(rooms):
        if f == floors:
            lead = 'L'
        elif f % 2 == 0:
            lead = 'O'
        else:
            lead = 'A'

        print(f'{lead}{f}{r}', end=' ')
        time.sleep(1)

    print('! Will print new line')  # '', end='\n'
