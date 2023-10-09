speed = float(input())

# •	При скорост до 10 (включително) отпечатайте "slow"
if speed <= 10:
    print("slow")
elif speed <= 50:  # speed is between 10 & 50; (10; 50]
    print("average")
elif speed <= 150:  # speed is between 50 & 150; (50; 150]
    print("fast")
elif speed <= 1000:  # speed is between 150 & 1000; (150; 1000]
    print("ultra fast")
else:                # speed is above 1000
    print("extremely fast")
