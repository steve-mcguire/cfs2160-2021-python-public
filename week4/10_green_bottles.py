#!/usr/bin/python3
__author__  = "Steve McGuire"
__contact__ = "s.mcguire@hud.ac.uk"

# Solution to week 4 GIS material tasks, please see slides in the week 5 GIS folder on BS
# This programme is used to print the lyrics for the popular child's counting song 10 green bottles
# https://www.youtube.com/watch?v=T0ooQv7oHvw
# it uses a loop and a function called within the loop to correctly print the lyrics.
# For and while loops used with different results


# function to deal with the pluralisation of bottles,
# note it just decides whether or not to add a letter 's' to the output
def pluralise(number):
    if number != 1:
        return "s"
    return ""


# the main loop to print the lyrics n (usually 10) times, starts at 10 and counts down to zero with increment of -1
# when counting down the increment must be specified for the range function to work.
print("With for loop")
for bottle in range(10, 0, -1):
    # inner loop to print the lien twice, removes code repetition
    for x in range(2):
        print(bottle, "green bottle" + pluralise(bottle) + " hanging on a wall,")
    print("And if 1 green bottle should accidentally fall,")
    print("They'll be " + str(bottle - 1) + " green bottle" + pluralise(bottle) + " hanging on a wall.\n")


# with while loop, although we know how many time the loop needs to happen,
#  e have a decision to make with regards to the printing of the number of bottles and them being pluralised.
# decisions indeed.
print("\n")
print("With while loop")
bottle = 10
while bottle >= 0:
    # inner loop to print the lien twice, removes code repetition
    for x in range(2):
        print(bottle, "green bottle" + pluralise(bottle) + " hanging on a wall,")
    print("And if 1 green bottle should accidentally fall,")
    print("They'll be " + str(bottle - 1) + " green bottle" + pluralise(bottle) + " hanging on a wall.\n")

    bottle -= 1