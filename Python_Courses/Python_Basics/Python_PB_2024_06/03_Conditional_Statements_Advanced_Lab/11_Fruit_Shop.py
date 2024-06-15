fruit = input()  # banana / apple / orange / grapefruit / kiwi / pineapple / grapes
day_of_week = input()  # Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday
quantity = float(input())

is_input_valid = True
price = 0
if (day_of_week == 'Monday'
        or day_of_week == 'Tuesday'
        or day_of_week == 'Wednesday'
        or day_of_week == 'Thursday'
        or day_of_week == 'Friday'):
    if fruit == 'banana':
        price = 2.50
    elif fruit == 'apple':
        price = 1.20
    elif fruit == 'orange':
        price = 0.85
    elif fruit == 'grapefruit':
        price = 1.45
    elif fruit == 'kiwi':
        price = 2.70
    elif fruit == 'pineapple':
        price = 5.50
    elif fruit == 'grapes':
        price = 3.85
    else:
        is_input_valid = False

elif day_of_week == 'Saturday' or day_of_week == 'Sunday':
    if fruit == 'banana':
        price = 2.70
    elif fruit == 'apple':
        price = 1.25
    elif fruit == 'orange':
        price = 0.90
    elif fruit == 'grapefruit':
        price = 1.60
    elif fruit == 'kiwi':
        price = 3.00
    elif fruit == 'pineapple':
        price = 5.60
    elif fruit == 'grapes':
        price = 4.20
    else:
        is_input_valid = False
else:
    is_input_valid = False

# if price != 0:
#     total_price = price * quantity
#     print(f'{total_price :.2f}')
# else:
#     print('error')

if is_input_valid:
    total_price = price * quantity
    print(f'{total_price :.2f}')
else:
    print('error')