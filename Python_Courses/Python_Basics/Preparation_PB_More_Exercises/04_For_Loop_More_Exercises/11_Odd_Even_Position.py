import sys

odd_sum = 0
odd_min = sys.maxsize
odd_max = - sys.maxsize
even_sum = 0
even_min = sys.maxsize
even_max = - sys.maxsize

numbers = int(input())

for i in range(1, numbers + 1):
    current_number = float(input())
    if i % 2 == 0:
        even_sum += current_number
        if current_number > even_max:
            even_max = current_number
        if current_number < even_min:
            even_min = current_number
    else:
        odd_sum += current_number
        if current_number > odd_max:
            odd_max = current_number
        if current_number < odd_min:
            odd_min = current_number

print(f"OddSum={odd_sum :.2f},")
print(f"OddMin={odd_min :.2f},") if not odd_min == sys.maxsize else print("OddMin=No,")
print(f"OddMax={odd_max :.2f},") if not odd_max == - sys.maxsize else print("OddMax=No,")
print(f"EvenSum={even_sum :.2f},")
print(f"EvenMin={even_min :.2f},") if not even_min == sys.maxsize else print("EvenMin=No,")
print(f"EvenMax={even_max :.2f}") if not even_max == - sys.maxsize else print("EvenMax=No")
