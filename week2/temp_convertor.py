#!/usr/bin/python3
__author__  = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

c = int(input("Enter Celsius temp"))
f = (c * 9/5) + 32
print(c,"Celsius is",f,"Fahrenheit ")

f = int(input("Enter Celsius temp"))
c = (f - 32) * 5/9
print(f,"Fahrenheit is",c ,"Celsius ")