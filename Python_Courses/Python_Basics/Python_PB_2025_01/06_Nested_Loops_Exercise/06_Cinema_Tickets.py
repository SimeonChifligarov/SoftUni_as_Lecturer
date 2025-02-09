student_count = 0
standard_count = 0
kid_count = 0

command = input()  # 'Finish' or movie, e.g. 'Taxi'

while command != 'Finish':
    movie = command

    seats_available = int(input())
    seats_taken = 0

    ticket_type = input()  # ticket_type OR 'End'
    while ticket_type != 'End':  # ("student", "standard", "kid")
        if ticket_type == 'student':
            student_count += 1
        elif ticket_type == 'standard':
            standard_count += 1
        elif ticket_type == 'kid':  # else:
            kid_count += 1

        seats_taken += 1

        if seats_taken >= seats_available:
            break

        ticket_type = input()

    percent_full = seats_taken / seats_available * 100
    print(f'{movie} - {percent_full:.2f}% full.')

    command = input()

total_tickets_count = student_count + standard_count + kid_count
percent_student = student_count / total_tickets_count * 100
percent_standard = standard_count / total_tickets_count * 100
percent_kid = kid_count / total_tickets_count * 100

print(f'Total tickets: {total_tickets_count}')
print(f'{percent_student:.2f}% student tickets.')
print(f'{percent_standard:.2f}% standard tickets.')
print(f'{percent_kid:.2f}% kids tickets.')
