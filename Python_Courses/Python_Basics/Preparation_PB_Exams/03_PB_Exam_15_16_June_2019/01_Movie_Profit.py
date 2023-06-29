movie_name = input()
days = int(input())
tickets_count = int(input())
ticket_price = float(input())
cinema_percent = int(input()) / 100

total_profit = tickets_count * ticket_price * days * (1 - cinema_percent)

print(f"The profit from the movie {movie_name} is {total_profit :.2f} lv.")
