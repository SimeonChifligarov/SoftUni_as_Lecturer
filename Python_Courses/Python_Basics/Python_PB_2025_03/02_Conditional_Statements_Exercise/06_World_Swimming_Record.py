# 1.	Рекордът в секунди – реално число;
record_seconds = float(input())
# 2.	Разстоянието в метри – реално число;
distance = float(input())
# 3.	Времето в секунди, за което плува разстояние от 1 м. - реално число.
time_per_meter = float(input())

swimming_time = distance * time_per_meter

# съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди.
delay_count = distance // 15  # 151 -> 10
delay_time = delay_count * 12.5

total_time = swimming_time + delay_time

if total_time < record_seconds:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    difference_seconds = total_time - record_seconds
    print(f'No, he failed! He was {difference_seconds:.2f} seconds slower.')
