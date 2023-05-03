pages = int(input())
pages_per_hour = int(input())
days = int(input())

total_hours_needed = pages // pages_per_hour

hours_per_day = total_hours_needed // days

print(hours_per_day)
