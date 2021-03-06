'''
2e.
Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of
a string so that all lowercase letters should come first.
For example:
Given: "WAtErmvEloN"
Expected Output: trmvloWAEEN
Hint: use lower() or upper() methods to check the case. Use join() to join both strings together.
'''

def sort_case(str):
    lower = []
    upper = []
    for char in str:
        if char.islower():
            lower.append(char)
        elif char.isupper():
            upper.append(char)
    lower.sort()
    upper.sort()
    return "".join(lower + upper)


print(sort_case("WAtErmvEloN"))