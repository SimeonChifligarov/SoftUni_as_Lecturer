# до получаване на команда  "NoMoreMoney"
total_sum = 0

command = input()  # "NoMoreMoney" or "3.56"
while command != "NoMoreMoney":
    current_num = float(command)  # float('3.56') == 3.56
    if current_num < 0:
        print('Invalid operation!')
        break

    print(f'Increase: {current_num :.2f}')

    total_sum += current_num  # 0 => 3.56

    command = input()

print(f'Total: {total_sum :.2f}')
