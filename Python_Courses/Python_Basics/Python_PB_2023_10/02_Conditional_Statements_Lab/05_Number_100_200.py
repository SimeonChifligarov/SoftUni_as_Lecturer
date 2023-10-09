number = int(input())

if number < 100:
    print("Less than 100")
elif number <= 200:  # number >= 100 and number < 200:  # if number is between 100 & 200
    print("Between 100 and 200")
else:
    print("Greater than 200")


# # Wrong CODE BELOW
# if number <= 200:
#     print("Between 100 and 200")
# elif number < 100:
#     print("Less than 100")
# else:
#     print("Greater than 200")