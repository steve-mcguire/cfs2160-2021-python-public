for x in range(0, 51):
    if x % 5 == 0 and x % 3 == 0:
        print("FizzBuzz", x, " ", x / 3, " ", x / 5)
    elif x % 5 == 0:
        print("Buzz", x, " ", x / 5)
    elif x % 3 == 0:
        print("Fizz", x, " ", x / 3)
    else:
        print(x)
