TOM_PLAY_NORM = 30_000
WORKDAY_PLAY_TIME = 63
HOLIDAY_PLAY_TIME = 127
DAYS_IN_A_YEAR = 365

holidays = int(input())
workdays = DAYS_IN_A_YEAR - holidays

total_play_time = holidays * HOLIDAY_PLAY_TIME + workdays * WORKDAY_PLAY_TIME

if total_play_time <= TOM_PLAY_NORM:
    below_play_time = TOM_PLAY_NORM - total_play_time
    below_play_hours = below_play_time // 60
    below_play_minutes = below_play_time % 60

    print("Tom sleeps well")
    print(f"{below_play_hours} hours and {below_play_minutes} minutes less for play")
else:
    above_play_time = total_play_time - TOM_PLAY_NORM
    above_play_hours = above_play_time // 60
    above_play_minutes = above_play_time % 60

    print("Tom will run away")
    print(f"{above_play_hours} hours and {above_play_minutes} minutes more for play")