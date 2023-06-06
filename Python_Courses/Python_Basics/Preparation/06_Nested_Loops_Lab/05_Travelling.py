command = input()
while not command == "End":
    city = command
    money_needed = float(input())
    total_money = 0
    while total_money < money_needed:
        total_money += float(input())

    print(f"Going to {city}!")

    command = input()
