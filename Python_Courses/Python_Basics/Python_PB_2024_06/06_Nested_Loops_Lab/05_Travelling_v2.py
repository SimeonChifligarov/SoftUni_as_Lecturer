command = input()  # "End" or {dest}
while command != "End":
    dest = command
    budget_needed = float(input())

    money = 0
    while money < budget_needed:
        money += float(input())

    print(f"Going to {dest}!")

    command = input()
