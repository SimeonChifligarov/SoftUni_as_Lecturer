command = input()

standard_count = 0
student_count = 0
kid_count = 0

while not command == "Finish":
    movie_name = command
    available_spaces = int(input())
    taken_seats = 0
    is_end = False
    for num in range(available_spaces):
        ticket = input()
        if ticket == "End":
            percent_full = taken_seats / available_spaces * 100
            print(f"{movie_name} - {percent_full:.2f}% full.")
            is_end = True
            command = input()
            break
        elif ticket == "standard":
            standard_count += 1
            taken_seats += 1
        elif ticket == "student":
            student_count += 1
            taken_seats += 1
        elif ticket == "kid":
            kid_count += 1
            taken_seats += 1

    if not is_end:
        percent_full = taken_seats / available_spaces * 100
        print(f"{movie_name} - {percent_full:.2f}% full.")
        command = input()
