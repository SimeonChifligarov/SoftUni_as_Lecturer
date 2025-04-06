# total_tickets_bought = 0
student_tickets_count = 0
standard_tickets_count = 0
kid_tickets_count = 0

# •	На първия ред до получаване на командата "Finish" - име на филма – текст
command = input()  # 'Finish' OR movie
while command != 'Finish':
    movie = command  # 'Scary movie'

    # •	На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]
    seats_available = int(input())
    # •	За всеки филм, се чете по един ред до изчерпване на свободните места в залата
    # или до получаване на командата "End":
    tickets_bought = 0
    # o	Типа на закупения билет - текст ("student", "standard", "kid")
    ticket_type = input()
    while ticket_type != 'End':
        tickets_bought += 1
        # total_tickets_bought += 1

        if ticket_type == 'student':
            student_tickets_count += 1
        elif ticket_type == 'standard':
            standard_tickets_count += 1
        elif ticket_type == 'kid':  # else:
            kid_tickets_count += 1

        if tickets_bought >= seats_available:
            break

        ticket_type = input()

    percent_full = tickets_bought / seats_available * 100
    print(f'{movie} - {percent_full:.2f}% full.')

    command = input()

total_tickets_bought = student_tickets_count + standard_tickets_count + kid_tickets_count

student_tickets_percent = student_tickets_count / total_tickets_bought * 100
standard_tickets_percent = standard_tickets_count / total_tickets_bought * 100
kid_tickets_percent = kid_tickets_count / total_tickets_bought * 100

print(f'Total tickets: {total_tickets_bought}')
print(f'{student_tickets_percent:.2f}% student tickets.')
print(f'{standard_tickets_percent:.2f}% standard tickets.')
print(f'{kid_tickets_percent:.2f}% kids tickets.')
