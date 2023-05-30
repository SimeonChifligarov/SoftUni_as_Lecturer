student_name = input()

current_class = 1
sum_grades = 0
failed = 0

while current_class <= 12:
    grade = float(input())
    if grade < 4:
        failed += 1
        if failed >= 2:
            break
        continue

    sum_grades += grade
    current_class += 1

average_grade = sum_grades / 12

if failed < 2:
    print(f"{student_name} graduated. Average grade: {average_grade :.2f}")
else:
    print(f"{student_name} has been excluded at {current_class} grade")
