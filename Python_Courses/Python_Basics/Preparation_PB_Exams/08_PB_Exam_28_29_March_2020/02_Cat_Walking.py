minutes_per_walk = int(input())
walking_count = int(input())
calories = int(input())

minutes_walking = minutes_per_walk * walking_count
calories_walking = minutes_walking * 5

if calories_walking >= calories / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_walking}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_walking}.")
