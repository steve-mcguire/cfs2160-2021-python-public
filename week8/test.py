def func_my(lst):
    num = lst[0]
    for a in lst:
        if a < num:
            num = a
    return num


print(func_my([1, 2, -8, 0]))

