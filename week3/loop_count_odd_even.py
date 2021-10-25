#!/usr/bin/python3
__author__  = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

numbers = [12, 75, 150, 180, 145, 525, 50]

odd = 0
even = 0

for x in numbers:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1

print(odd, "odd,", even, "even.")