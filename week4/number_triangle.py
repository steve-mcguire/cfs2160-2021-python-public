#!/usr/bin/python3
__author__  = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

row = int(input("How many rows? "))
for x in range(1, row + 1):
    for y in range(1, x + 1):
        print(y, end=" ")
    print("")