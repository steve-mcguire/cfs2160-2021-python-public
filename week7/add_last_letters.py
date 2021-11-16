'''
2d.
Add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing'
then add 'ly' at the end of it. If the string length of the given string is less than 3, leave it unchanged.
For example:
Given: toast
Expected Output: toasting
Given: sing
Expected Output: singly
Given: si
Expected Output: si (length is less than 3. Leave it unchanged)
Hint: use str1[-3:] to check the ending of the string for ‘ing’.
'''


def ing_ly(str):
    if len(str) >= 3:
        if str[-3:] == "ing":
            str += "ly"
        else:
            str += "ing"
    return str


print(ing_ly("sing"))
print(ing_ly("toast"))
print(ing_ly("si"))
print(ing_ly("driving"))
