UPPER_BOUNDARY = 50
LOWER_BOUNDARY = 0

up_to_9_count = 0
up_to_19_count = 0
up_to_29_count = 0
up_to_39_count = 0
up_to_50_count = 0
invalid_count = 0
total_score = 0

moves = int(input())


for _ in range(moves):
    current_move = int(input())
    # if current_move < LOWER_BOUNDARY or current_move > UPPER_BOUNDARY:
    if not (LOWER_BOUNDARY <= current_move <= UPPER_BOUNDARY):
        invalid_count += 1
        total_score /= 2
    elif current_move > 39:
        up_to_50_count += 1
        total_score += 100
    elif current_move > 29:
        up_to_39_count += 1
        total_score += 50
    elif current_move > 19:
        up_to_29_count += 1
        total_score += current_move * 0.40
    elif current_move > 9:
        up_to_19_count += 1
        total_score += current_move * 0.30
    else:  # elif current_move > 0:
        up_to_9_count += 1
        total_score += current_move * 0.20


print(f"{total_score :.2f}")
print(f"From 0 to 9: {up_to_9_count / moves :.2%}")
print(f"From 10 to 19: {up_to_19_count / moves :.2%}")
print(f"From 20 to 29: {up_to_29_count / moves :.2%}")
print(f"From 30 to 39: {up_to_39_count / moves :.2%}")
print(f"From 40 to 50: {up_to_50_count / moves :.2%}")
print(f"Invalid numbers: {invalid_count / moves :.2%}")
