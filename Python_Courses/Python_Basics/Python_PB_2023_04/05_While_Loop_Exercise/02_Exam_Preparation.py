COMMAND_FOR_END = "Enough"
NOT_GOOD_THRESHOLD = 4

total_grades = 0
count_grades = 0
count_not_good_grades = 0
last_problem_name = ""

not_good_grades_count_threshold = int(input())

is_failed = False
while True:
    command = input()
    if command == COMMAND_FOR_END:
        break

    last_problem_name = command
    problem_grade = int(input())
    total_grades += problem_grade
    count_grades += 1

    if problem_grade <= NOT_GOOD_THRESHOLD:
        count_not_good_grades += 1
        if count_not_good_grades >= not_good_grades_count_threshold:
            is_failed = True
            break


avg_grade = total_grades / count_grades

if not is_failed:
    print(f"Average score: {avg_grade :.2f}")
    print(f"Number of problems: {count_grades}")
    print(f"Last problem: {last_problem_name}")
else:
    print(f"You need a break, {count_not_good_grades} poor grades.")
