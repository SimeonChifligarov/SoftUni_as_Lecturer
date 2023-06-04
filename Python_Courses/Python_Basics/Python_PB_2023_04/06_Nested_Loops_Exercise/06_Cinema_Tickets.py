total_tickets = 0
students_total = 0
standard_total = 0
kids_total = 0

command = input()  # "Finish" OR "current_movie_name"
while not command == "Finish":
    current_movie = command
    total_seats = int(input())
    available_seats = total_seats

    while available_seats > 0:
        current_ticket_type = input()  # "End" OR some of these - ["student", "standard", "kid"]

        if current_ticket_type == "End":
            break

        available_seats -= 1
        # total_tickets += 1
        if current_ticket_type == "student":
            students_total += 1
        elif current_ticket_type == "standard":
            standard_total += 1
        elif current_ticket_type == "kid":
            kids_total += 1

    seats_bought = total_seats - available_seats
    total_tickets += seats_bought

    percent_full = seats_bought / total_seats * 100
    print(f"{current_movie} - {percent_full :.2f}% full.")

    command = input()


percent_students = students_total / total_tickets * 100
percent_standard = standard_total / total_tickets * 100
percent_kids = kids_total / total_tickets * 100

print(f"Total tickets: {total_tickets}")
print(f"{percent_students :.2f}% student tickets.")
print(f"{percent_standard :.2f}% standard tickets.")
print(f"{percent_kids :.2f}% kids tickets.")
