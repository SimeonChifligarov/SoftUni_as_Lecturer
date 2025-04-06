total_sum = 0
judges_score_count = 0

# От конзолата на първият ред се прочита броят на хората в журито n - цяло число.
judges = int(input())
# След това на отделен ред се прочита името на презентацията – текст OR 'Finish'

command = input()  # 'Finish' OR current_presentation
while command != 'Finish':
    # За всяка една презентация на нов ред се четат n - на брой оценки - реално число.
    current_presentation = command  # ...

    current_presentation_score = 0
    for _ in range(judges):  # e.g. range(2):  [0, 1]
        judges_score_count += 1

        judge_score = float(input())
        current_presentation_score += judge_score

    total_sum += current_presentation_score
    current_presentation_avg = current_presentation_score / judges
    print(f'{current_presentation} - {current_presentation_avg:.2f}.')

    command = input()

final_score = total_sum / judges_score_count
print(f'Student\'s final assessment is {final_score:.2f}.')
