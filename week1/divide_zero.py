#!/usr/bin/python3
__author__  = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

x = 0
y = 60

if y == 0:
    print("cant to that mate")
else:
    print(x / y)

try:
    print(y / x, "r")
except ZeroDivisionError as z:
    print(z)

number_of_pupils = 16
number_of_sweets = 47

print(number_of_sweets // number_of_pupils)
print(number_of_sweets % number_of_pupils)

'''

number_of_pupils = input("Please enter the number of pupils")
number_of_sweets = input("Please enter the number of Sweets")

print(type(number_of_sweets))
print(type(number_of_pupils))

number_of_sweets = int(number_of_sweets)
number_of_pupils = int(number_of_pupils)

print(type(number_of_sweets))
print(type(number_of_pupils))
'''