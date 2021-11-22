'''
2b.
Write a Python function to get a string from a given string where all occurrences of its first char have been changed
to '$', except the first char itself.
For example:
Input restart becomes resta$t where except the first character, all occurrences of the first character change to $.
Hint: use replace() method.
'''

def replace_all_instance(str):
    first = str[0].lower()
    r = str.replace(first, "$")
    return first + r[1:]


print(replace_all_instance("restart"))
