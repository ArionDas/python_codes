# waps to find the angles of a triangle when three sides are given. Enter the lengths using input() function.
import math
a = int(input())
b = int(input())
c = int(input())

cos_a = (b**2 + c**2 - a**2)/(2*b*c)
ang_a = math.acos(cos_a)

cos_b = (a**2 + c**2 - b**2)/(2*a*c)
ang_b = math.acos(cos_b)

cos_c = (a**2 + b**2 - c**2)/(2*a*b)
ang_c = math.acos(cos_c)

print("The angles are")

print(math.degrees(ang_a))
print(math.degrees(ang_b))
print(math.degrees(ang_c))
