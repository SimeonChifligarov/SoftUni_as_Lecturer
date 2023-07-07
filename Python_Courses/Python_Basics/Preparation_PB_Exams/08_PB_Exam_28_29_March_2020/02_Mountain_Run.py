record_in_seconds = float(input())
distance = float(input())
seconds_per_meter = float(input())

total_seconds = distance * seconds_per_meter
extra_seconds = (distance // 50) * 30

total_seconds += extra_seconds

if total_seconds < record_in_seconds:
    print(f"Yes! The new record is {total_seconds :.2f} seconds.")
else:
    print(f"No! He was {total_seconds - record_in_seconds :.2f} seconds slower.")
