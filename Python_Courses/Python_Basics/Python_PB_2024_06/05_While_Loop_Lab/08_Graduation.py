student = input()

grades_sum = 0
current_class = 1
fails_count = 0
is_graduated = True

while current_class <= 12:
    grade = float(input())
    if grade < 4:
        fails_count += 1
        if fails_count >= 2:
            is_graduated = False
            break
        continue

    grades_sum += grade
    current_class += 1

# is_graduated = fails_count < 2
if is_graduated:
    avg_grade = grades_sum / 12
    print(f'{student} graduated. Average grade: {avg_grade :.2f}')
else:
    print(f'{student} has been excluded at {current_class} grade')
