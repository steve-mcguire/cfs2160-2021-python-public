#!/usr/bin/python3
__author__  = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

numbers = [12, 75, 150, 180, 145, 525, 50]


for x in numbers:
    if x > 500:
        break
    elif x > 150:
        continue
    elif x % 5 == 0:
        print(x)
