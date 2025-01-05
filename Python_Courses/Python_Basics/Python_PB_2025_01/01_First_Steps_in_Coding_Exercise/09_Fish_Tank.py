# Един литър вода се равнява на един кубичен дециметър/ 1л=1 дм3/.

# 1.	Дължина в см – цяло число в интервала [10 … 500]
length = int(input())
# 2.	Широчина в см – цяло число в интервала [10 … 300]
width = int(input())
# 3.	Височина в см – цяло число в интервала [10… 200]
height = int(input())
# 4.	Процент  – реално число в интервала [0.000 … 100.000]
percent_not_empty = float(input())  # 17.0

total_volume = length * width * height  # in cm^3
total_volume_in_liters = total_volume / 1000

liters_needed = total_volume_in_liters * (1 - percent_not_empty / 100)

print(liters_needed)
