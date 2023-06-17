UNKNOWN_MESSAGE = "unknown"

degrees = float(input())

if degrees < 5 or degrees > 35:
    print(UNKNOWN_MESSAGE)
elif degrees >= 26:
    print("Hot")
elif degrees > 20:
    print("Warm")
elif degrees >= 15:
    print("Mild")
elif degrees >= 12:
    print("Cool")
elif degrees >= 5:  # else:
    print("Cold")
