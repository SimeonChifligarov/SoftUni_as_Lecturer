# 03 Harvest - Conditional Statements - Extra

from math import floor, ceil

area = int(input())
grapes_per_meter = float(input())
needed_litres = int(input())
workers = int(input())

available_area = 0.4 * area
grapes_for_litre = 2.5

total_grapes = available_area * grapes_per_meter
wine = total_grapes / grapes_for_litre

diff = 0
if wine < needed_litres:
    diff = floor(needed_litres - wine)
    print(f"It will be a tough winter! More {diff} liters wine needed.")
elif wine >= needed_litres:
    diff = ceil(wine - needed_litres)
    per_person = ceil(diff / workers)
    print(f"Good harvest this year! Total wine: {int(wine)} liters.")
    print(f"{diff} liters left -> {per_person} liters per person.")
