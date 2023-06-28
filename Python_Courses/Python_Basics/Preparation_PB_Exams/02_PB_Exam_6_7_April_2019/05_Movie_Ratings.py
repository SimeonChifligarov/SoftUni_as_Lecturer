total_ratings = 0
best_rating = 0
best_movie = ""
lowest_rating = 11
lowest_movie = ""

movies_count = int(input())

for _ in range(movies_count):
    movie = input()
    movie_rating = float(input())

    total_ratings += movie_rating
    if movie_rating >= best_rating:
        best_rating = movie_rating
        best_movie = movie
    if movie_rating <= lowest_rating:
        lowest_rating = movie_rating
        lowest_movie = movie

avg_rating = total_ratings / movies_count

print(f"{best_movie} is with highest rating: {best_rating :.1f}")
print(f"{lowest_movie} is with lowest rating: {lowest_rating :.1f}")
print(f"Average rating: {avg_rating :.1f}")
