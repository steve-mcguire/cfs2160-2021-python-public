def do_sum(exp):
    if len(exp) != 3:
        raise ValueError("Your input does not have three characters")
    else:
        try:
            # perform the sum
            x = int(exp[0])
            y = int(exp[2])
            operand = exp[1]
            if operand == "+":
                return x + y
            elif operand == "-":
                return x - y
            else:
                raise ValueError("Your operand is not recognised")
        except ValueError:
            raise ValueError("Your input contains illegal characters")


while True:
    try:
        user_input = input("Enter your sum").split(" ")
        print(do_sum(user_input))
    except ValueError as ve:
        print(ve)


