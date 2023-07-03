high_jump_target = int(input())

current_target = high_jump_target - 30
jumps = 0
fails = 0

is_success = False
while True:
    jumps += 1
    current_high_jump = int(input())
    if current_high_jump > current_target:
        if current_target >= high_jump_target:
            is_success = True
            break
        current_target += 5
        fails = 0
    else:
        fails += 1
        if fails >= 3:
            break

if is_success:
    print(f"Tihomir succeeded, he jumped over {high_jump_target}cm after {jumps} jumps.")
else:
    print(f"Tihomir failed at {current_target}cm after {jumps} jumps.")
