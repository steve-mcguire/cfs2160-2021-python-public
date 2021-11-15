
#a_list = ["Steve", "Ebony", "Cameron", "Zhaoxuan"]
def countdown(start):
    '''
    a function that counts down to zero
    :return:
    '''
    if start != 0:
        print(start)
        countdown(start - 1)
    else:
        print("finished")


countdown(10)
print("After function")

for x in range(10, 0, -1):
    print(x)