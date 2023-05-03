length = int(input("insert length: "))
width = int(input("insert width: "))
height = int(input("insert height: "))
percent_non_empty = float(input("insert percent_non_empty: "))

total_volume = length * width * height  # държи cm^3
total_volume_in_liters = total_volume / 1000  # / 1л=1 дм3/.

water_needed = total_volume_in_liters * (100 - percent_non_empty) / 100

print(water_needed)
