str1 = 'melon'
print("Original String is", str1)

# Get first character
first = str1[0]

# Get string size
l = len(str1)
# Get middle index number
middle = int(l / 2)
# Get middle character and add it to result
first = first + str1[middle]
last = str1[l - 1]

# Get last character and add it to result
first = first + last

print("New String:", first)
