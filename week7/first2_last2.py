'''
2a.
Get a string made of the first 2 and the last 2 characters from a user input string.
If the string length is less than 2, return empty string instead.
For example:
User input String : ‘watermelon’
Expected Result : 'waon'
User input String: 'wa'
Expected Result : 'wawa'
User input String: 'w'
Expected Result : Empty String
Hint: use string slicing and concatenation.
'''
def f2_and_l2(str):
    if len(str) < 2:
        return "Empty String"
    else:
        return  str[:2] + str[-2:]

print(f2_and_l2("wa"))



