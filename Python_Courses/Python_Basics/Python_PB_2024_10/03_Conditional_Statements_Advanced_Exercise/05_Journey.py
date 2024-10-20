budget = float(input())
season = input()  # "summer” or "winter”

destination = ''
vacation_type = ''
vacation_cost = 0.0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        vacation_cost = budget * 0.30
        vacation_type = 'Camp'
    elif season == 'winter':
        vacation_cost = budget * 0.70
        vacation_type = 'Hotel'

elif budget <= 1000:  # (100; 1000]
    destination = 'Balkans'
    if season == 'summer':
        vacation_cost = budget * 0.40
        vacation_type = 'Camp'
    elif season == 'winter':
        vacation_cost = budget * 0.80
        vacation_type = 'Hotel'

else:  # (1000, inf)
    destination = 'Europe'
    vacation_cost = budget * 0.90
    vacation_type = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{vacation_type} - {vacation_cost :.2f}')
