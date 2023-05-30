POOR_GRADE_THRESHOLD = 4

failed_count = 0
total_grades = 0
problems_count = 0
last_problem_name = ""
is_failed = False

failed_count_boundary = int(input())

while True:
    problem_name = input()
    if problem_name == "Enough":
        break

    last_problem_name = problem_name
    problem_score = int(input())

    total_grades += problem_score
    problems_count += 1

    if problem_score <= POOR_GRADE_THRESHOLD:
        failed_count += 1
        if failed_count >= failed_count_boundary:
            is_failed = True
            break

if not is_failed:
    avg_grade = total_grades / problems_count
    print(f"Average score: {avg_grade :.2f}")
    print(f"Number of problems: {problems_count}")
    print(f"Last problem: {last_problem_name}")
else:
    print(f"You need a break, {failed_count} poor grades.")
