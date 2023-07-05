import math

SUGAR_GR = 950
FLOUR_GR = 750

easter_breads = int(input())

total_sugar = 0
total_flour = 0
max_sugar = 0
max_flour = 0
for _ in range(easter_breads):
    sugar = int(input())
    flour = int(input())

    total_sugar += sugar
    total_flour += flour
    if sugar > max_sugar:
        max_sugar = sugar
    if flour > max_flour:
        max_flour = flour

total_sugar_packets = math.ceil(total_sugar / SUGAR_GR)
total_flour_packets = math.ceil(total_flour / FLOUR_GR)

print(f"Sugar: {total_sugar_packets}")
print(f"Flour: {total_flour_packets}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
