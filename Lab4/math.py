import math as m
#task 1
n = float(input("degree?:"))
print(f"Radian{(m.pi * n/180): .6f}")

#task 2
h = int(input("height:"))
b1 = int(input("base 1:"))
b2 = int(input("base 2:"))
print(f"Expected Output:{(b1  + b2)/2 * h}")

#task 3 
from math import tan, pi
a = float(input("Input number of sides: "))
b = float(input("Input the length of a side: "))
print(f'The area of the polygon is: {a * b**2 / 4 / tan(pi/a): .1f}')

#task 4
b = int(input("Length of base:"))
c = int(input("Height of parallelogram:"))
print(f"Expected Output:{(b*c)}")