# password in the form of "{A}{B}{x}{y}{B}{A}"

passwords = []

a = int(input())
b = int(input())
max_generated_passwords = int(input())

A = 35
B = 64
counter = 1
should_break = False
for x in range(1, a + 1):
    for y in range(1, b + 1):
        current_password = f"{chr(A + counter - 1)}{chr(B + counter - 1)}" \
                           f"{x}{y}" \
                           f"{chr(B + counter - 1)}{chr(A + counter - 1)}"

        passwords.append(current_password)

        A += 1
        B += 1
        if A > 55:
            A = 35
        if B > 96:
            B = 64

        if len(passwords) >= max_generated_passwords:
            should_break = True
            break
    if should_break:
        break


print("|".join(passwords), end="|")
