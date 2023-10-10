world_record = float(input())
distance = float(input())
time_per_meter = float(input())

distance_required_in_seconds = distance * time_per_meter
water_resistance = distance // 15 * 12.5

total_time = distance_required_in_seconds + water_resistance

if total_time >= world_record:
    print(f'No, he failed! He was {total_time - world_record:.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
