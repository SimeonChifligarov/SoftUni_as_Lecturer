total_scores = 0
total_presentations = 0

judges_count = int(input())

command = input()
while not command == "Finish":
    current_presentation = command
    current_score = 0
    for score in range(judges_count):
        current_score += float(input())

    total_scores += current_score
    total_presentations += 1

    print(f"{current_presentation} - {current_score / judges_count :.2f}.")

    command = input()

avg_score = total_scores / (total_presentations * judges_count)
print(f"Student's final assessment is {avg_score :.2f}.")
