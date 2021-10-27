import random as rand

secret = rand.randrange(0, 101)
guesses = 0
while True:
    guesses += 1
    guess = int(input("Guess a number between zero and 100"))
    if secret == guess:
        print("Well done")
        break
    elif guess > secret:
        print("Your number is too big, guess again")
    else:
        print("Your number is too small, guess again")

print("You took", guesses, "guesses")
