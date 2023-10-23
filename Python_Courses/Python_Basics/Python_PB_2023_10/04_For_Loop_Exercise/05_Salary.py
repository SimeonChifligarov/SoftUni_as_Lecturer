opened_tabs_count = int(input())
salary = float(input())  # should be int?

# is_salary = True
for _ in range(opened_tabs_count):  # [0, 1, 2, ..., opened_tabs_counts - 1];
    current_website = input()

    if current_website == "Facebook":
        salary -= 150
    elif current_website == "Instagram":
        salary -= 100
    elif current_website == "Reddit":
        salary -= 50

    if salary <= 0:
        # is_salary = False
        print("You have lost your salary.")
        break
else:
    print(int(salary))
