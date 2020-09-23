#!/usr/bin/env python3
#https://github.com/nidhiwalia/bch5884
import math

x=input("Please enter temp in fahrenheit")
x=int(x)
print(x)
print(type(x))

y=x-32
z=y*5/9
r=z+273.15
r=round(r,2)
print(r)
print("the ans is in kelvin")
