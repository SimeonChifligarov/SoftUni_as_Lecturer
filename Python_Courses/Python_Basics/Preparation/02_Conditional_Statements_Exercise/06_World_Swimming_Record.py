slowdown_in_seconds = 12.5

record_in_seconds = float(input())
distance_in_meters = float(input())
seconds_for_a_meter = float(input())

slowdowns_count = distance_in_meters // 15

slowdown_seconds = slowdowns_count * slowdown_in_seconds

seconds_final = distance_in_meters * seconds_for_a_meter + slowdown_seconds

if seconds_final < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {seconds_final :.2f} seconds.")
else:
    print(f"No, he failed! He was {seconds_final - record_in_seconds :.2f} seconds slower.")
