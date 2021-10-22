#!/usr/bin/python3
__author__  = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

x = int(input("Enter number 1"))
y = int(input("Enter number 2"))

if x > y:
    print("first number is greater than second")
elif x == y:
    print("both are equal")
else: # X < Y
    print("first number is less than second")