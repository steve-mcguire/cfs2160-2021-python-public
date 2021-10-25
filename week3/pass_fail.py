#!/usr/bin/python3
__author__  = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

score = 50
pass_mark = 40
day = "Tuesday"


if type(score) == pass_mark or day == "Tuesday":
    # this is inside the if
    print("You have passed")
else:
    print("You have not passed")

print("nested if")

day = "Monday"
time = "PM"

if day == "Monday":
    if time == "AM":
        print("It is Monday morning")
    else:
        print("It is Monday afternoon")
else:
    print("today is not Monday")


print("compound check")

if day == "Monday" and time == "AM":
    print("It is Monday morning")
elif day == "Monday" and time != "AM":
    print("It is Monday afternoon")
else:
    print("It is not Monday")