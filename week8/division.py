def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        raise ZeroDivisionError("One of your numbers is zero")
    except TypeError:
        raise TypeError("At least one of your values is not a number")