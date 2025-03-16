budget = float(input())
season = input()  # "summer” or "winter”

destination = ''
vacation_type = ''
total_cost = 0.0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        total_cost = budget * 0.30  # Лято - 30% от бюджета
        vacation_type = 'Camp'
    elif season == 'winter':
        total_cost = budget * 0.70 # Зима - 70% от бюджета
        vacation_type = 'Hotel'

elif budget <= 1_000:  # (100; 1000]
    destination = 'Balkans'
    if season == 'summer':
        total_cost = budget * 0.40  # Лято - 40% от бюджета
        vacation_type = 'Camp'
    elif season == 'winter':
        total_cost = budget * 0.80  # Зима - 80% от бюджета
        vacation_type = 'Hotel'
else:  # (1000; +inf)
    destination = 'Europe'
    total_cost = budget * 0.90  # независимо от сезона, ще похарчи 90% от бюджета
    vacation_type = 'Hotel'  # aко е в Европа, независимо от сезона, ще почива в хотел
    # if season == 'summer':
    #     total_cost = budget * 0.90  # независимо от сезона, ще похарчи 90% от бюджета
    #     vacation_type = 'Hotel'
    # elif season == 'winter':
    #     total_cost = budget * 0.90  # независимо от сезона, ще похарчи 90% от бюджета
    #     vacation_type = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{vacation_type} - {total_cost:.2f}')
