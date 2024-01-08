# / 1л=1 дм3/.

# 1.	Дължина в см – цяло число в интервала [10 … 500]
length = int(input())
# 2.	Широчина в см – цяло число в интервала [10 … 300]
width = int(input())
# 3.	Височина в см – цяло число в интервала [10… 200]
height = int(input())
# 4.	Процент  – реално число в интервала [0.000 … 100.000]
percent_taken = float(input())

percent_taken_as_percent = percent_taken / 100
total_volume = length * width * height / 1000 # cm^3 / 1000 == дм^3 == l
liters_needed = total_volume * (1 - percent_taken_as_percent)

# изчислява литрите вода, която са необходими за напълването на аквариума.
print(liters_needed)
