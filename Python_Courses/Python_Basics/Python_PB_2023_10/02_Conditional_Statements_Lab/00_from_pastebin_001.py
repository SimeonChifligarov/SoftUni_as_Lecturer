speed = float(input())

range1 = (-0.0, 10.01)
range2 = (10.01, 50.01)
range3 = (50.01, 150.01)
range4 = (150.01, 1000.01)
range5 = (1000.01, float('inf'))

if range1[0] <= speed < range1[1]:
    print('slow')
elif range2[0] <= speed < range2[1]:
    print('average')
elif range3[0] <= speed < range3[1]:
    print('fast')
elif range4[0] <= speed < range4[1]:
    print('ultra fast')
elif range5[0] <= speed < range5[1]:
    print('extremely fast')
else:
    print('slow')
