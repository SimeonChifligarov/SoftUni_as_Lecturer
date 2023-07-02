control_minutes = int(input())
control_seconds = int(input())

track_length = float(input())
seconds_per_100m = int(input())

control_total_seconds = control_minutes * 60 + control_seconds
player_total_seconds = track_length / 100 * seconds_per_100m - track_length / 120 * 2.5

if player_total_seconds <= control_total_seconds:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {player_total_seconds :.3f}.")
else:
    print(f"No, Marin failed! He was {player_total_seconds - control_total_seconds :.3f} second slower.")
