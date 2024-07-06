# четат първо дестинацията и минималния бюджет (десетично число),

# destination = input()
# budget_needed = float(input())
#
# money = 0
# while money < budget_needed:
#     current_saving = float(input())
#     money += current_saving
#
# print(f'Going to {destination}!')

command = input()  # {destination} or "End"
while command != "End":
    destination = command
    budget_needed = float(input())

    money = 0
    while money < budget_needed:
        current_saving = float(input())
        money += current_saving

    print(f'Going to {destination}!')

    command = input()
