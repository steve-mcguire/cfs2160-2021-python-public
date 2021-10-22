my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in my_list:
    # divide i by 2 will give a number for 10, 30, 50 etc
    # if that number module 2 is zero then it must be in even index
    if i / 2 % 2 != 0:
        print(i)

print("steve"[1::2])
