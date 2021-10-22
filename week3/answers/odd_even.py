#!/usr/bin/python3
__author__  = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

odd = 0
even = 0
for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print(even, "even numbers,", odd, "numbers")