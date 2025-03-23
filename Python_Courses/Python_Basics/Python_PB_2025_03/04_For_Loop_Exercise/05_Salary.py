opened_tabs = int(input())
salary = float(input())

for _ in range(opened_tabs):  # [0, 1,... opened_tabs) == [0, ... opened_tabs - 1]
    current_tab = input()

    if current_tab == 'Facebook':
        salary -= 150
        if salary <= 0:
            break
    elif current_tab == 'Instagram':
        salary -= 100
        if salary <= 0:
            break
    elif current_tab == 'Reddit':
        salary -= 50
        if salary <= 0:
            break


if salary <= 0:
    print('You have lost your salary.')
else:
    print(int(salary))
