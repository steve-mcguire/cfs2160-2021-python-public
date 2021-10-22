#!/usr/bin/python3
__author__  = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"


def c_to_f(c):
    f = c * 9/5 + 32
    return f


def f_to_c(f):
    c = (f - 32) * 5/9
    return c


print(c_to_f(37))
print(f_to_c(98.6))