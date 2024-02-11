judges_count = int(input())
total_score = 0
total_grades = 0

command = input()
while command != "Finish":  # 'Finish' OR current_presentation
    current_presentation = command

    current_presentation_total = 0
    for _ in range(judges_count):  # 2 => [0, 1]
        current_score = float(input())
        current_presentation_total += current_score

    avg_score = current_presentation_total / judges_count
    print(f'{current_presentation} - {avg_score :.2f}.')

    total_score += current_presentation_total
    total_grades += judges_count
    command = input()

avg_total_score = total_score / total_grades
print(f"Student's final assessment is {avg_total_score :.2f}.")
