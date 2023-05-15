mammals = [
    "dog",
]

reptiles = [
    "crocodile",
    "tortoise",
    "snake",
]

animal = input()

if animal in mammals:
    print("mammal")
elif animal in reptiles:
    print("reptile")
else:
    print("unknown")
