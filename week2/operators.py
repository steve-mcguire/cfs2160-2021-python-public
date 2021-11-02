#!/usr/bin/python3
__author__  = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

num1 = int('3.14')
print (num1)

name = "Steve"
print(type(name))
print(name)
age = 43
print(type(age))
print(age)
height = 5.11
print(type(height))
print(height)

print(name == "Steve") # is equal to / comparison
print(name == "Steve" and age == 19)

has_license = False

print(has_license and age >= 17)

if has_license and age >= 17:
    print("You can hire a car")
else:
    print("You cannot hire a car")

