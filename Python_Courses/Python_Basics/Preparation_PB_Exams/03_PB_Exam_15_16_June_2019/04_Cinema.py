TICKET_PRICE = 5

hall_capacity = int(input())

seats_left = hall_capacity
total_income = 0
command = input()
while command != "Movie time!":
    tickets = int(command)
    if tickets > seats_left:
        break
    seats_left -= tickets
    total_income += tickets * TICKET_PRICE
    if tickets % 3 == 0:
        total_income -= 5

    command = input()

if command == "Movie time!":
    print(f"There are {seats_left} seats left in the cinema.")
else:
    print("The cinema is full.")

print(f"Cinema income - {total_income} lv.")
