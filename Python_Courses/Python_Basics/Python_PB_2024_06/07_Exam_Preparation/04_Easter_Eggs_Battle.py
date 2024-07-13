END_COMMAND = 'End'

p1_eggs = int(input())
p2_eggs = int(input())

command = input()
while command != END_COMMAND:
    if command == 'one':
        p2_eggs -= 1
        if p2_eggs == 0:
            print(f'Player two is out of eggs. Player one has {p1_eggs} eggs left.')
            break

    elif command == 'two':
        p1_eggs -= 1
        if p1_eggs == 0:
            print(f'Player one is out of eggs. Player two has {p2_eggs} eggs left.')
            break

    command = input()

if command == 'End':
    print(f"Player one has {p1_eggs} eggs left.")
    print(f"Player two has {p2_eggs} eggs left.")
