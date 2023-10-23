exam_hour = int(input())
exam_minutes = int(input())
arriving_hour = int(input())
arriving_minutes = int(input())

exam_time = exam_hour * 60 + exam_minutes
arriving_time = arriving_hour * 60 + arriving_minutes
diff = abs(arriving_time - exam_time)

if arriving_time > exam_time:
    print("Late")
elif arriving_time == exam_time or abs(diff) <= 30:
    print("On time")
elif abs(diff) > 30:
    print("Early")

hh = diff // 60
mm = diff % 60

if diff != 0:
    if arriving_time < exam_time and abs(diff) < 60:
        print(f"{abs(diff)} minutes before the start")

    elif arriving_time < exam_time and abs(diff) >= 60:
        print(f"{hh}:{mm :02d} hours before the start")

    elif arriving_time > exam_time and abs(diff) < 60:
        print(f"{diff} minutes after the start")

    elif arriving_time > exam_time and abs(diff) >= 60:
        print(f"{hh}:{mm:02d} hours after the start")
