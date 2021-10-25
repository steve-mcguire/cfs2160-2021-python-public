#!/usr/bin/python3
__author__  = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue # ignores all code after and go to the next pointer in the loop
    print(i)
