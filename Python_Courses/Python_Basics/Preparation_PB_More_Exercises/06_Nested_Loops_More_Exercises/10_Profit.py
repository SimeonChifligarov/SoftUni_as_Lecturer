ones = int(input())
twos = int(input())
fives = int(input())
target = int(input())

for i in range(ones + 1):
    for j in range(twos + 1):
        for k in range(fives + 1):
            if i * 1 + j * 2 + k * 5 == target:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {target} lv.")
