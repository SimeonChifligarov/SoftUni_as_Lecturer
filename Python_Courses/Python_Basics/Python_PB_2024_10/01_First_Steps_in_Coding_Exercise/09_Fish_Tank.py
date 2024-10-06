# Един литър вода се равнява на един кубичен дециметър/ 1л=1 дм3/.

length = int(input())  # cm
width = int(input())
height = int(input())
not_empty_percent = float(input())

total_volume = length * width * height  # in cm * cm * cm == cm^3
total_volume_in_liters = total_volume / 1000  # 1l == 1 dm^3 == 1000 cm^3

total_liters_needed = total_volume_in_liters * (1 - not_empty_percent / 100)  # 17 % => 0.17

print(total_liters_needed)
