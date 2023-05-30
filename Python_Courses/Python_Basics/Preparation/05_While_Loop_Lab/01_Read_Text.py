# # Solution 1
# string = input()
#
# while string != "Stop":
#     print(string)
#     string = input()

# Solution 2
STOP_STRING = "Stop"

string = input()
while not string == STOP_STRING:
    print(string)
    string = input()
