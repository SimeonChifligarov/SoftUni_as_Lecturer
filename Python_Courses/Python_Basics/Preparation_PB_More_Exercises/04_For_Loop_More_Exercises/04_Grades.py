total_grades = 0
above_5 = 0  # including 5.00
above_4 = 0
above_3 = 0
failed = 0

students_count = int(input())

for _ in range(students_count):
    student_grade = float(input())
    total_grades += student_grade
    if student_grade >= 5:
        above_5 += 1
    elif student_grade >= 4:
        above_4 += 1
    elif student_grade >= 3:
        above_3 += 1
    else:
        failed += 1

print(f"Top students: {above_5 / students_count :.2%}")
print(f"Between 4.00 and 4.99: {above_4 / students_count :.2%}")
print(f"Between 3.00 and 3.99: {above_3 / students_count :.2%}")
print(f"Fail: {failed / students_count :.2%}")
print(f"Average: {total_grades / students_count :.2f}")
