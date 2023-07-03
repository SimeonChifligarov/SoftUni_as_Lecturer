# refactor using dictionary {"back": back_count, ...}

back_count = 0
chest_count = 0
legs_count = 0
abs_count = 0
protein_shake_count = 0
protein_bar_count = 0

visitors = int(input())

for _ in range(visitors):
    activity = input()  # "Back", "Chest", "Legs", "Abs", "Protein shake", "Protein bar"
    if activity == "Back":
        back_count += 1
    elif activity == "Chest":
        chest_count += 1
    elif activity == "Legs":
        legs_count += 1
    elif activity == "Abs":
        abs_count += 1
    elif activity == "Protein shake":
        protein_shake_count += 1
    elif activity == "Protein bar":
        protein_bar_count += 1

work_out_count = back_count + chest_count + legs_count + abs_count
protein_count = protein_shake_count + protein_bar_count

print(f"{back_count} - back")
print(f"{chest_count} - chest")
print(f"{legs_count} - legs")
print(f"{abs_count} - abs")
print(f"{protein_shake_count} - protein shake")
print(f"{protein_bar_count} - protein bar")
print(f"{work_out_count / visitors :.2%} - work out")
print(f"{protein_count / visitors :.2%} - protein")
