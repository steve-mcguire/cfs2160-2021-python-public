num1 = 10
operand = "/"
num2 = 20
if operand in ["+", "-", "*"]:
    print("in then list 1")
else:
    print("an error")


if operand == "+" or operand == "-" or operand == "*":
    print("in then list 2")

else:
    print("an error")