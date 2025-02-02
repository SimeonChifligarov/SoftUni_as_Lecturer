balance = 0.0

data = input()
while data != 'NoMoreMoney':

    if data == 'NoMoreMoney':
        print(f'Total: {balance:.2f}')
        break

    elif float(data) <= 0:
        print('Invalid operation!')
        break
    else:
        print(f'Increase: {float(data):.2f}')
        balance += float(data)

    data = input()

print(f'Total: {balance:.2f}')
