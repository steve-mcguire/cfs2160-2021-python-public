#!/usr/bin/python3
__author__  = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        print("Break")
        break
    elif num > 150:
        print(num, "continue")
        continue
    elif num % 5 == 0:
        print(num, "Mod 5")

