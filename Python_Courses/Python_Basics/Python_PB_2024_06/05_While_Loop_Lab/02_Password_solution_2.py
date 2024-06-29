username = input()
password = input()

while True:
    guess = input()
    if guess == password:
        break

print(f'Welcome {username}!')
