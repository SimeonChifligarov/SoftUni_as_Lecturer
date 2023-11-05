student_tickets = 0
standard_tickets = 0
kid_tickets = 0

command = input()  # "Finish" OR movie_name
while command != "Finish":
    movie_name = command
    total_seats = int(input())

    ticket_bought = 0
    ticket_type = input()  # "End" OR ticket_type IN ("student", "standard", "kid")
    while ticket_type != "End":
        ticket_bought += 1

        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1

        if ticket_bought == total_seats:
            break

        ticket_type = input()

    percent_full = ticket_bought / total_seats * 100
    print(f"{movie_name} - {percent_full :.2f}% full.")

    command = input()


total_tickets = student_tickets + standard_tickets + kid_tickets
print(f"Total tickets: {total_tickets}")
print(f"{student_tickets / total_tickets * 100 :.2f}% student tickets.")
print(f"{standard_tickets / total_tickets * 100 :.2f}% standard tickets.")
print(f"{kid_tickets / total_tickets * 100 :.2f}% kids tickets.")
