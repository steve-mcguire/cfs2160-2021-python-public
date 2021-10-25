#!/usr/bin/python3
__author__  = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

# get input from user and store in variable (radius)
# process the input to int
# convert radius to area using equaision
# print the results

import math
import steve_math as sm

radius = int(input("Please enter the radius of a circle"))

#area = math.pi * radius ** 2

area = sm.area_of_circle(radius)

#print(round(2.1))
#print(math.ceil(2.1))

print(round(2.7))
print(math.floor(2.7))

print(area)