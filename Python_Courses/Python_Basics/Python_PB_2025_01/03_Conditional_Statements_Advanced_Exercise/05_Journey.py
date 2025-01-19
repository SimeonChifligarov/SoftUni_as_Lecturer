budget = float(input())
season = input()  # "summer” or "winter"

destination = ''
price = 0.0
vacation_type = ''

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        price = 0.30 * budget
        vacation_type = 'Camp'
    elif season == 'winter':  # else:
        price = 0.70 * budget
        vacation_type = 'Hotel'
elif budget <= 1000:  # (100; 1000]
    destination = 'Balkans'
    if season == 'summer':
        price = 0.40 * budget
        vacation_type = 'Camp'
    elif season == 'winter':  # else:
        price = 0.80 * budget
        vacation_type = 'Hotel'
elif budget > 1000:  # else:  (1000; +inf)
    destination = 'Europe'
    # price = 0.90 * budget
    # vacation_type = 'Hotel'
    if season == 'summer':
        price = 0.90 * budget
        vacation_type = 'Hotel'
    elif season == 'winter':  # else:
        price = 0.90 * budget
        vacation_type = 'Hotel'


print(f'Somewhere in {destination}')
print(f'{vacation_type} - {price:.2f}')
