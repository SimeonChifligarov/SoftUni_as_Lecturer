name = input()
year_grade = float(input())
years_graduated = 0
tries = 0
total_grade = 0

while years_graduated < 12:
    if year_grade < 4:
        tries += 1
        if tries >= 2:
            break
    else:
        years_graduated += 1
        total_grade += year_grade
    if years_graduated == 12:
        break
    year_grade = float(input())

average_grade = total_grade / 12

if years_graduated < 12:
    print(f"{name} has been excluded at {years_graduated + 1} grade")
else:
    print(f"{name} graduated. Average grade: {average_grade:.2f}")