#!/usr/bin/python3
__author__  = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

x = int(input("Enter your start number"))

total = 0
for y in range(1, x+1):
    total += y

print(total)