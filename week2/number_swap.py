#!/usr/bin/python3
__author__  = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

# declare variables and assign values
x = 10
y = 20

print("Before swap")
print(x, "x")
print(y, "y")

z = y # store y in z for temp
y = x # switch y and x
x = z # put z into x
print("After swap with third var")
print(x, "x")
print(y, "y")

# assign x to y and y to x in single line, allows swapping without third value as the values are swapped in
# memory before being finalised when run.
x, y = y, x

print("After swap without third var (swap back to original values)")
print(x, "x")
print(y, "y")
