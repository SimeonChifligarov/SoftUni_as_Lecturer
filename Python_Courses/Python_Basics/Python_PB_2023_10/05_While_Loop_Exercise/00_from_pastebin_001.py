student_name = input()
boolean = True
low_grade = 0
total = 0
year = 1

while boolean:
    year_grades = float(input())
    if year_grades < 4:
        low_grade += 1
        if low_grade > 1:
            print(f"{student_name} has been excluded at {year} grade")
            break
        continue
    if year_grades >= 4:
        year += 1

    total += year_grades
    if year > 12:
        print(f"{student_name} graduated. Average grade: {total / 12:.2f}")
        break
