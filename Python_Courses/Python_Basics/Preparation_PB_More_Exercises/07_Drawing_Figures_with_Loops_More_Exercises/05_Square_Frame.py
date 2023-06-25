result = []

square_frame_side = int(input())

for i in range(square_frame_side):
    if i == 0 or i == square_frame_side - 1:
        row = f"+ {'- ' * (square_frame_side - 2)}+"
        result.append(row)
    else:
        row = f"| {'- ' * (square_frame_side - 2)}|"
        result.append(row)

print(*result, sep='\n')
