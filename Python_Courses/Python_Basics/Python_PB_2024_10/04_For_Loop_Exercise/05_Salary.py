# •	"Facebook" -> 150 лв.
# •	"Instagram" -> 100 лв.
# •	"Reddit" -> 50 лв.

opened_tabs = int(input())  # 4
salary = float(input())

for _ in range(opened_tabs):  # for tab in range(4):  [0, 1, 2, 3]
    current_tab = input()  # 'Facebook', ...
    if current_tab == 'Facebook':
        salary -= 150
    elif current_tab == 'Instagram':
        salary -= 100
    elif current_tab == 'Reddit':
        salary -= 50

    if salary <= 0:
        break

if salary <= 0:
    print('You have lost your salary.')
else:
    print(int(salary))
