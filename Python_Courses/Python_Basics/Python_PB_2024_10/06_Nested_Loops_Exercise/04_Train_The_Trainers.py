# От конзолата на първият ред се прочита броят на хората в журито n - цяло число.
judges_count = int(input())

total_sum = 0
presentation_count = 0
# След това на отделен ред се прочита името на презентацията – текст.
command = input()
while command != 'Finish':  # 'Finish' or current_presentation (e.g. 'While loop')
    current_presentation = command
    presentation_count += 1

    current_sum = 0
    # За всяка една презентация на нов ред се четат n - на брой оценки - реално число.
    for _ in range(judges_count):
        judge_score = float(input())  # e.g. float('5.50') == 5.50
        current_sum += judge_score

    avg_score = current_sum / judges_count
    print(f'{current_presentation} - {avg_score :.2f}.')

    total_sum += current_sum

    command = input()

total_avg_score = total_sum / (judges_count * presentation_count)
print(f'Student\'s final assessment is {total_avg_score :.2f}.')
