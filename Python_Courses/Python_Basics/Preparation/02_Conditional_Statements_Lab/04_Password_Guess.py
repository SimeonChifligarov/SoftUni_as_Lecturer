REAL_PASSWORD = "s3cr3t!P@ssw0rd"

WRONG_PASSWORD_MESSAGE = "Wrong password!"
WELCOME_MESSAGE = "Welcome"

entry_password = input()

print(WELCOME_MESSAGE) if entry_password == REAL_PASSWORD else print(WRONG_PASSWORD_MESSAGE)
