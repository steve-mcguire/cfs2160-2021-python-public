#!/usr/bin/python3
__author__  = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

string = "CFS2160-2021-Python"

digits = []
letters = []
other = []

for value in string:
    if value.isalpha():
        letters.append(value)
    elif value.isdigit():
        digits.append(value)
    else:
        other.append(value)

print(letters, len(letters))
print(digits, len(digits))
print(other, len(other))

