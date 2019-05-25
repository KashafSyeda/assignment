print("the distance between the points (x1, y1) and (x2, y2)")
import math
x1 = int(input("enter value of x1: "))
x2 = int(input("enter value of x2: "))
y1 = int(input("enter value of y1: "))
y2 = int(input("enter value of y2: "))
d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
print(d)