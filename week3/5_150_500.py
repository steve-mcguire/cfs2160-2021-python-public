#!/usr/bin/python3
__author__  = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"



numbers = [12, 75, 150, 180, 145, 525, 50]

for number in numbers:
    if number > 500:
        break
    elif number > 150:
        continue
    elif number % 5 == 0:
        print(number, "% 5")