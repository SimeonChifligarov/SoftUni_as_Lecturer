# 1. E
total_pages = int(input())
pages_per_hour = int(input())
days = int(input())

# 2. T
total_hours_needed = total_pages // pages_per_hour
hours_per_day = total_hours_needed / days

# 3. L
print(int(hours_per_day))  # int(7.0) == 7
