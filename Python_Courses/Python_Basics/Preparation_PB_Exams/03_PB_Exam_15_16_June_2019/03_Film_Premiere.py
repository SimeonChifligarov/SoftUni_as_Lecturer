movies = {
    "John Wick": {
        "Drink": 12,
        "Popcorn": 15,
        "Menu": 19,
    },
    "Star Wars": {
        "Drink": 18,
        "Popcorn": 25,
        "Menu": 30,
    },
    "Jumanji": {
        "Drink": 9,
        "Popcorn": 11,
        "Menu": 14,
    },
}

movie_name = input()  # "John Wick", "Star Wars", or "Jumanji"
movie_package = input()  # "Drink", "Popcorn", or "Menu"
tickets_count = int(input())

ticket_price = movies[movie_name][movie_package]

total_price = ticket_price * tickets_count

if movie_name == "Star Wars" and tickets_count >= 4:
    total_price *= (1 - 0.30)

if movie_name == "Jumanji" and tickets_count == 2:
    total_price *= (1 - 0.15)

print(f"Your bill is {total_price :.2f} leva.")
