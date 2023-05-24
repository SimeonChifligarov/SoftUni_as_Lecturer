import sys

smallest = sys.maxsize
biggest = -sys.maxsize

num_count = int(input())
for _ in range(num_count):
    num = int(input())
    if num < smallest:
        smallest = num
    if num > biggest:
        biggest = num

print(f"Max number: {biggest}")
print(f"Min number: {smallest}")
