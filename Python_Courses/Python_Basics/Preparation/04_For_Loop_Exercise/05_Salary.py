FACEBOOK_FINE = 150
INSTAGRAM_FINE = 100
REDDIT_FINE = 50

opened_tabs = int(input())
salary = int(input())
is_salary_lost = False
for _ in range(opened_tabs):
    current_website = input()

    if current_website == "Facebook":
        salary -= FACEBOOK_FINE
        if salary <= 0:
            is_salary_lost = True
            break
    elif current_website == "Instagram":
        salary -= INSTAGRAM_FINE
        if salary <= 0:
            is_salary_lost = True
            break
    elif current_website == "Reddit":
        salary -= REDDIT_FINE
        if salary <= 0:
            is_salary_lost = True
            break

if is_salary_lost:
    print("You have lost your salary.")
else:
    print(salary)
