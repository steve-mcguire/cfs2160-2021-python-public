'''
2b.
Write a Python function to get a string from a given string where all occurrences of its first char have been changed
to '$', except the first char itself.
For example:
Input 'restart' becomes 'resta$t' where except the first character, all occurrences of the first character change to $.
Hint: use replace() method.
'''


def replace_first_char(str):
    first_char = str[0].lower()
    new_str = str.replace(first_char, "$")
    return first_char + new_str[1:]


'''while True:
    print("Type END to finish")
    response = input("Type a word to replace char: ")
    if response.upper() == "END":
        print("Programme terminated")
        break
    else:
        print(replace_first_char(response))'''


words = ["restart", "trotter", "steve", "test", "Rahamahn", "Oliver"]

for word in words:
    print(replace_first_char(word))
