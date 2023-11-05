lucky_number = int(input())
first = 0
second = 0
third = 0
fourth = 0
sum1 = 1
sum2 = 1
while sum1 != lucky_number % sum1 == 0 and sum2 != lucky_number % sum1 == 0:
    for first in range(1, 10):
        for second in range(1, 10):
            sum1 = first + second
            if lucky_number % sum1 == 0:
                for third in range(1, 10):
                    for fourth in range(1, 10):
                        sum2 = third + fourth
                        if lucky_number % sum2 == 0:
                            if sum1 == sum2:
                                print(f"{first}{second}{third}{fourth}", end=" ")
