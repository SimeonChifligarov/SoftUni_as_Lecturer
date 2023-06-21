SUCCESSFUL_TRANSACTION_MSG = "Product sold!"
FAILED_TRANSACTION_MSG = "Error in transaction!"
END_COMMAND = "End"


money_target = int(input())
money_total_cs = 0
money_total_cc = 0
money_total = 0
buyers_cs = 0
buyers_cc = 0
current_buyer = 0
is_success = False

command = input()
while not command == END_COMMAND:
    current_money = int(command)
    current_buyer += 1
    if current_money < 10 and current_buyer % 2 == 0:
        print(FAILED_TRANSACTION_MSG)
    elif current_money > 100 and not current_buyer % 2 == 0:
        print(FAILED_TRANSACTION_MSG)
    else:
        money_total += current_money
        print(SUCCESSFUL_TRANSACTION_MSG)
        if current_buyer % 2 == 0:
            money_total_cc += current_money
            buyers_cc += 1
        else:
            money_total_cs += current_money
            buyers_cs += 1
        if money_total >= money_target:
            is_success = True
            break

    command = input()

if is_success:
    print(f"Average CS: {money_total_cs / buyers_cs :.2f}")
    print(f"Average CC: {money_total_cc / buyers_cc :.2f}")
else:
    print("Failed to collect required money for charity.")
