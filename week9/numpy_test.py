import numpy as np
import random as rand


ocean = np.zeros((5,5))
print(ocean)


x = rand.randint(0, 5)
y = rand.randint(0, 5)
ocean[x, y] = 1
print(ocean)

while True:
    guess_x = int(input("Enter x"))
    guess_y = int(input("Enter y"))
    if ocean[guess_x, guess_y] == 1:
        print("You sunk my battleship!")
    else:
        ocean[guess_x, guess_y] = "x"
    print(ocean)
