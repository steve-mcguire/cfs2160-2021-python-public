#!/usr/bin/python3
__author__  = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

# fibonacci calculator
x = 0
y = 1

for i in range(50):
    
    print(x)
    temp = x + y
    x = y
    y = temp


