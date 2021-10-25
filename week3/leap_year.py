#!/usr/bin/python3
__author__  = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

year = 2104
print(year % 4)
print(year % 100)
print(year % 400)

print("------------")
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(year, " is a leap year")
        else:
            print(year, " is not a leap year")
    else:
        print(year, " is a leap year")
else:
    print(year, " is not a leap year")