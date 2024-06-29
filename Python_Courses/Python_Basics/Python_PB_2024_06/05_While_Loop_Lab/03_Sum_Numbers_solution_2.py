boundary_number = int(input())

total_sum = 0
while True:
    current_number = int(input())
    total_sum += current_number
    
    if total_sum >= boundary_number:
        break

print(total_sum)
