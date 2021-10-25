#!/usr/bin/python3
__author__  = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

for x in range(0, 7):
    if x not in (3, 6):
        print(x)
    if x % 3 != 0:
        print(x)