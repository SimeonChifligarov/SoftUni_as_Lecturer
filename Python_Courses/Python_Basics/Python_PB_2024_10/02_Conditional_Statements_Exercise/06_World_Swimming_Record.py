# import math

record_seconds = float(input())
distance_in_meters = float(input())
seconds_per_meter = float(input())

# slowdown_seconds = math.floor(distance_in_meters / 15) * 12.5
slowdown_seconds = distance_in_meters // 15 * 12.5
swimming_seconds = distance_in_meters * seconds_per_meter

total_seconds = swimming_seconds + slowdown_seconds

if total_seconds < record_seconds:
    print(f'Yes, he succeeded! The new world record is {total_seconds :.2f} seconds.')
else:
    diff = total_seconds - record_seconds
    print(f'No, he failed! He was {diff :.2f} seconds slower.')
