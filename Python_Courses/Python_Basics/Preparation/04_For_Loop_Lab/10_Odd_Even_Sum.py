n = int(input())

odd_sum = 0
even_sum = 0
for i in range(1, n + 1):
    current_num = int(input())
    if i % 2 == 0:
        even_sum += current_num
    else:
        odd_sum += current_num

if even_sum == odd_sum:
    print(f"Yes\nSum = {even_sum}")
else:
    diff = abs(even_sum - odd_sum)
    print(f"No\nDiff = {diff}")
