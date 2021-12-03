import random as rand

# Generate random number between 0 to 100

# Pass all three arguments in randrange()
print("First Random Number: ", rand.randrange(-50, 100, 10))

# Pass first two arguments in randrange()
print("Second Random Number: ", rand.randrange(0, 100))
# Default step = 1

# Or, you can only pass the start argument
print("Third Random Number: ", rand.randint(100, 200))
# Default start = 0, step = 1

print("A random int", rand.randint(0, 100))

rand_list_int = rand.sample(range(0, 50), 6)
print(rand_list_int)
