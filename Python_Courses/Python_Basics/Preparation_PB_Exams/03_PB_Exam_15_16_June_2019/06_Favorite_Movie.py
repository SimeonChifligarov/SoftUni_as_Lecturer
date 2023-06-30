LIMIT = 7

best_movie = ""
best_movie_score = 0

counter = 0
command = input()
while command != "STOP":
    movie = command
    movie_score = 0
    for char in movie:
        movie_score += ord(char)
        if char.islower():
            movie_score -= 2 * len(movie)
        elif char.isupper():
            movie_score -= len(movie)

    if movie_score > best_movie_score:
        best_movie_score = movie_score
        best_movie = movie

    counter += 1
    if counter >= LIMIT:
        print("The limit is reached.")
        break
    command = input()

print(f"The best movie for you is {best_movie} with {best_movie_score} ASCII sum.")
