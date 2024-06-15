age = float(input())  # '13.05' -> float('13.05') == 13.05
gender = input()  # 'm' or 'f'

result = ''
if gender == 'm':
    if age >= 16:
        result = 'Mr.'
    else:
        result = 'Master'
elif gender == 'f':
    if age >= 16:
        result = 'Ms.'
    else:
        result = 'Miss'

print(result)
