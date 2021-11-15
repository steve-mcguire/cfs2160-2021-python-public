def odd_or_even(value):
    '''
    Checks to see if a given value is odd or even
    :return: Boolean True or False
    '''
    try:
        if value % 2 == 0:
            #print("Even")
            return True
        else:
            #print("Odd")
            return False
    except TypeError as te:
        print(te)

print(odd_or_even("c10"))
