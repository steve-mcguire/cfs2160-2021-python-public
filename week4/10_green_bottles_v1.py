def pluralise(bottle):
    if bottle != 1:
        return "s"
    else:
        return ""



for bottle in range(10, 0, -1):
    for x in range(2):
        print(bottle, "green bottle" + pluralise(bottle) + ", standing on a wall,")
    print("and if one green bottle should accidentally fall,")
    print("They'll be", bottle - 1 ,"green bottle" + pluralise(bottle-1) + " standing on a wall.\n")