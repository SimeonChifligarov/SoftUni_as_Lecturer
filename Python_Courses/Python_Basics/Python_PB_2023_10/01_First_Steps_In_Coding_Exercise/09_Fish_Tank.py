length = int(input())
width = int(input())
height = int(input())
percent_not_empty = float(input()) / 100  # 17 input means => 0.17 == 17%

fish_tank_volume = length * width * height  # cm * cm * cm == cm^3
fish_tank_volume_in_liters = fish_tank_volume / 1000  # dm^3 AND 1l == 1 dm^3

water_needed_liters = fish_tank_volume_in_liters * (1 - percent_not_empty)
print(water_needed_liters)
