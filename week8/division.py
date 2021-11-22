def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as z:
        raise ZeroDivisionError(z)



for x in range(0, 100):
    try:
        print(divide(10, x))
    except Exception as e:
        print(type(e), e)