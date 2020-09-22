#!/usr/bin/env python3
#https://github.com/nidhiwalia/bch5884


import math
x1=input("enter x value of point A:")
y1=input("enter y value of point A:")

x2=input("enter x value of point B:")
y2=input("enter y value of point B:")

x3=input("enter x value of point C:")
y3=input("enter y value of point C:")

x1=int(x1)
y1=int(y1)
x2=int(x2)
y2=int(y2)
x3=int(x3)
y3=int(y3)


dx1=x1-x2
dy1=y1-y2

dx2=x2-x3
dy2=y2-y3

dx3=x3-x1
dy3=y3-y1

d1=math.sqrt(dx1**2+dy1**2)
d1=round(d1,2)
print("side1 is", d1)

d2=math.sqrt(dx2**2+dy2**2)
d2=round(d2,2)
print("side2 is", d2)

d3=math.sqrt(dx3**2+dy3**2)
d3=round(d3,2)
print("side3 is",d3)


a=(d2**2+d3**2-d1**2)/(2*d2*d3)
a=float(a)

angle=math.acos(a)
angle1=math.degrees(angle)
angle1=round(angle1,2)
print("first angle value in degrees is:",angle1)

b=(d3**2+d1**2-d2**2)/(2*d3*d1)
b=float(b)

angle2=math.acos(b)
secondangle=math.degrees(angle2)
secondangle=round(secondangle,2)
print("second angle value in degrees is:",secondangle)

d=180-(angle1+secondangle)
d=round(d,2)
print("third angle value in degrees is:",d)






