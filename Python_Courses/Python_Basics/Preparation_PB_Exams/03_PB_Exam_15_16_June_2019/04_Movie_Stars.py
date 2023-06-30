total_budget = float(input())

budget_left = total_budget
command = input()
while command != "ACTION":
    actor = command
    if len(actor) > 15:
        actor_salary = budget_left * 0.20
    else:
        actor_salary = float(input())
    budget_left -= actor_salary
    if budget_left < 0:
        break

    command = input()

if budget_left < 0:
    print(f"We need {-budget_left :.2f} leva for our actors.")
else:
    print(f"We are left with {budget_left :.2f} leva.")
