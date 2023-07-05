starting_eggs = int(input())

current_eggs = starting_eggs
sold_eggs = 0
is_empty = False
command = input()
while command != "Close":
    eggs_count = int(input())
    if command == "Buy":
        if eggs_count > current_eggs:
            is_empty = True
            break
        current_eggs -= eggs_count
        sold_eggs += eggs_count

    elif command == "Fill":
        current_eggs += eggs_count

    command = input()

if is_empty:
    print("Not enough eggs in store!")
    print(f"You can buy only {current_eggs}.")
else:
    print("Store is closed!")
    print(f"{sold_eggs} eggs sold.")
