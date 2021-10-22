#!/usr/bin/python3
__author__  = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

# capture input() from user
radius = input("Please enter the radius of a circle")
# convert to int()
radius = int(radius)
# calculate the area
area = 3.141592653589793 * radius ** 2
# display the result
print(area)
