WELCOME_MESSAGE = "Welcome {}!"

username = input()
password = input()

password_guess = input()
while not password_guess == password:
    password_guess = input()

print(WELCOME_MESSAGE.format(username))
