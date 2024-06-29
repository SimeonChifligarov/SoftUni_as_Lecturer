# Напишете програма, която чете цяло число от конзолата
boundary_number = int(input())
# и на всеки следващ ред цели числа, докато тяхната сума
# стане по-голяма или равна на първоначалното число.
total_sum = 0
while total_sum < boundary_number:
    current_number = int(input())
    total_sum += current_number
# След приключване на четенето да се отпечата сумата на въведените числа.
print(total_sum)
