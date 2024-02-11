student_name = input()

marks = 0
year_counter = 0
is_failed = False
failed_counts = 0

while year_counter < 12:
    annual_mark = float(input())

    if annual_mark < 4:
        failed_counts += 1
        # is_failed = True

        if failed_counts >= 2:
            is_failed = True
            break
    else:
        marks += annual_mark
        year_counter += 1

if not is_failed:
    average_marks = marks / year_counter
    print(f"{student_name} graduated. Average grade: {average_marks :.2f}")
else:
    print(f"{student_name} has been excluded at {year_counter + 1} grade")