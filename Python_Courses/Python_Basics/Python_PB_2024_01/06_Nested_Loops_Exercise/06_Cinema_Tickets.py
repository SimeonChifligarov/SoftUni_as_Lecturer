# total_tickets = 0
total_student = 0
total_standard = 0
total_kids = 0

command = input()  # 'Finish' OR current_movie
while command != "Finish":
    current_movie = command
    total_seats = int(input())

    taken_seats = 0
    ticket_type = input()  # 'End' OR ticket_type -> ("student", "standard", "kid")
    while ticket_type != 'End':
        taken_seats += 1

        if ticket_type == "student":
            total_student += 1
        elif ticket_type == "standard":
            total_standard += 1
        elif ticket_type == "kid":
            total_kids += 1

        if taken_seats == total_seats:
            break

        ticket_type = input()

    percent_full = taken_seats / total_seats * 100
    print(f'{current_movie} - {percent_full :.2f}% full.')

    # total_tickets += taken_seats

    command = input()

total_tickets = total_student + total_standard + total_kids

percent_student = total_student / total_tickets * 100
percent_standard = total_standard / total_tickets * 100
percent_kids = total_kids / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{percent_student :.2f}% student tickets.")
print(f"{percent_standard :.2f}% standard tickets.")
print(f"{percent_kids :.2f}% kids tickets.")
