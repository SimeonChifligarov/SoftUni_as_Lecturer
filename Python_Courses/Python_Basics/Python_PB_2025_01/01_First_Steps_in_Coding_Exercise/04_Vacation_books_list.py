# 1.	Брой страници в текущата книга – цяло число в интервала [1…1000]
total_pages = int(input())
# 2.	Страници, които прочита за 1 час – цяло число в интервала [1…1000]
pages_per_hour = int(input())
# 3.	Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]
days = int(input())

total_hours_needed = total_pages // pages_per_hour
# print(total_hours_needed)
hours_per_day = total_hours_needed / days

print(hours_per_day)
