
def split_list(operand, value):
    return value.split(operand)


def do_addition(sum):
    try:
        return int(sum[0]) + int(sum[1])
    except Exception as e:
        raise Exception("You sum contains and error")


def do_subtraction(sum):
    try:
        return int(sum[0]) + int(sum[1])
    except Exception as e:
        raise Exception("Addition", e)


exp = input("Enter your sum")

if "+" in exp:
    try:
        exp_list = split_list("+", exp)
        print(do_addition(exp_list))
    except Exception as e:
        print("Subtraction", e)
elif "-" in exp:
    try:
        exp_list = split_list("-", exp)
        print(do_subtraction(exp_list))
    except Exception as e:
        print(e)
else:
    print("Sum not valid")
