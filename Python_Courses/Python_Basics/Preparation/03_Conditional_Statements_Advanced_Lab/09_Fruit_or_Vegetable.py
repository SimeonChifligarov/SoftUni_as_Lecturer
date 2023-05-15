fruits = [
    "banana",
    "apple",
    "kiwi",
    "cherry",
    "lemon",
    "grapes",
]

vegetables = [
    "tomato",
    "cucumber",
    "pepper",
    "carrot",
]

product = input()

if product in fruits:
    print("fruit")
elif product in vegetables:
    print("vegetable")
else:
    print("unknown")
