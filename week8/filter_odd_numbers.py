numbers = [7, 8, 120, 25, 44, 20, 27]
even = []
odd = []
x = 0
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print(even, " - ", odd)

# What would be the remaining items in the list 'num' after executing above code?
# the list is filtered as items are removed, this is why 120 remains in the list once the programme has completed
