movies = {
    "A Star Is Born": {
        "normal": 7.50,
        "luxury": 10.50,
        "ultra luxury": 13.50,
    },
    "Bohemian Rhapsody": {
        "normal": 7.35,
        "luxury": 9.45,
        "ultra luxury": 12.75,
    },
    "Green Book": {
        "normal": 8.15,
        "luxury": 10.25,
        "ultra luxury": 13.25,
    },
    "The Favourite": {
        "normal": 8.75,
        "luxury": 11.55,
        "ultra luxury": 13.95,
    },
}

movie_name = input()  # "A Star Is Born", "Bohemian Rhapsody","Green Book", or "The Favourite"
hall_type = input()  # "normal", "luxury", "ultra luxury"
tickets = int(input())

movie_price = movies[movie_name][hall_type]

total_income = tickets * movie_price

print(f"{movie_name} -> {total_income :.2f} lv.")
