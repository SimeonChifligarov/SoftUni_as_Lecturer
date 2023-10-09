number = int(input())

if number < 100:
    print('Less than 100')

# elif number >= 100 <= 200:
elif 100 >= number <= 200:  # FIX
    print('Between 100 and 200')

else:
    print('Greater than 200')
