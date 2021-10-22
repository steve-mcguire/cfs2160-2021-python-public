import random as rand

def odd_or_even(number):
    # we do some stuff
    result = number % 2 == 0
    return result


rand_list_int = rand.sample(range(0, 101), 10)
print(rand_list_int)

for number in rand_list_int:
    print(type(number))
    if odd_or_even(number):
        print("Even")
    else:
        print("Odd")

number = "10"
print(type(number))