def do_sum(exp):
    if len(exp) != 3:
        raise ValueError("You sum is not in the correct format")
    else:
        try:
            # do the thing if interest
            value_1 = float(exp[0])
            value_2 = float(exp[2])
            operand = exp[1]
            if operand == "+":
                return value_1 + value_2
            elif operand == "-":
                return value_1 - value_2
            else:
                raise ValueError("Your operand is not valid") # needs work

        except ValueError:
            raise ValueError("Your values are not all numbers")


while True:
    user_input = input("Please enter your sum").split(" ")
    try:
        print(do_sum(user_input))
    except ValueError as ve:
        print(ve)

print("PROGRAMME COMPLETED OK")

