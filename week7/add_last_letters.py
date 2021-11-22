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
Hint: use str1[-3:] to check the ending of the stirng for ‘ing’.

'''
import copy


def ing_ly(str):
    if len(str) >= 3:
        if str[-3:] == "ing":
            return str + "ly"
        else:
            return str + "ing"
    return str

list_of_words = ["toast", "toasting", "steve", "bo", "testing", "cfs2160"]
for word in list_of_words:
    print(ing_ly(word))

n = 300
m = copy.deepcopy(n)
print(id(n))
print(m is n)














