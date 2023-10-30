bad_grades_threshold = int(input())
total_score = 0
problems_count = 0
last_problem = ""
bad_grades_count = 0

# is_positive_result = False

command = input()
while command != "Enough":
    problem_name = command
    problem_grade = int(input())

    last_problem = problem_name
    total_score += problem_grade
    problems_count += 1

    if problem_grade <= 4:
        bad_grades_count += 1
        if bad_grades_count >= bad_grades_threshold:
            break

    command = input()

if command == "Enough":
    avg_score = total_score / problems_count
    print(f"Average score: {avg_score :.2f}")  # total_score / problems_count
    print(f"Number of problems: {problems_count}")
    print(f"Last problem: {last_problem}")
else:
    print(f"You need a break, {bad_grades_count} poor grades.")
