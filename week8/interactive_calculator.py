str = input("Enter your sum").split()
if str[1] == "+":
    print(int(str[0]) + int(str[2]))
elif str[1] == "-":
    print(int(str[0]) - int(str[2]))