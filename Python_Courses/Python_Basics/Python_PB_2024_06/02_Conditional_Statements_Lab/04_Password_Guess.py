# фразата "s3cr3t!P@ssw0rd".
# При съвпадение да се изведе "Welcome".
# При несъвпадение да се изведе "Wrong password!".

attempt = input()

if attempt == "s3cr3t!P@ssw0rd":
    print("Welcome")
else:
    print("Wrong password!")
