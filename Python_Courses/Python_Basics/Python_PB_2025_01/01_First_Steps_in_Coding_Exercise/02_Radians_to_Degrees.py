# градус = радиан * 180 / π
# Числото π в Python може да достъпите чрез модула math
# import math  # math.pi
from math import pi


# 1. прочитаме вход; + го кастваме към подходящия дата тип
radians = float(input())
# 2. правим математическото преобразувание
degrees = radians * 180 / pi
# 3. извеждаме на изхода
print(degrees)
