# from 11.11.2020

import math
fig_type = input()

if fig_type == "square":
    a = float(input())
    area = a * a
    print(f'{area:.3f}')

elif fig_type == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
    print(f'{area:.3f}')
elif fig_type == "circle":
    a = float(input())
    area = math.pi * a * a
    print(f'{area:.3f}')
elif fig_type == "triangle":
    a = float(input())
    h = float(input())
    area = a * h / 2
    print(f'{area:.3f}')
