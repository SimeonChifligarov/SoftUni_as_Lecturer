current_balance = 0

command = input()
while not command == "NoMoreMoney":
    current_sum = float(command)
    if current_sum < 0:
        print("Invalid operation!")
        break

    current_balance += current_sum
    print(f"Increase: {current_sum :.2f}")
    command = input()

print(f"Total: {current_balance :.2f}")
