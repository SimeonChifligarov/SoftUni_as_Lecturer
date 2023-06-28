student_count = 0
standard_count = 0
kid_count = 0

command = input()
while not command == "Finish":
    current_movie = command
    all_seats = int(input())
    available_seats = all_seats
    current_count = 0

    current_ticket = input()
    while not current_ticket == "End":
        if current_ticket == "student":
            student_count += 1
        elif current_ticket == "standard":
            standard_count += 1
        elif current_ticket == "kid":
            kid_count += 1

        current_count += 1
        available_seats -= 1
        if available_seats <= 0:
            break

        current_ticket = input()

    print(f"{current_movie} - {current_count / all_seats * 100 :.2f}% full.")

    command = input()

total_tickets = student_count + standard_count + kid_count
print(f"Total tickets: {total_tickets}")
print(f"{student_count / total_tickets * 100 :.2f}% student tickets.")
print(f"{standard_count / total_tickets * 100 :.2f}% standard tickets.")
print(f"{kid_count / total_tickets * 100 :.2f}% kids tickets.")
