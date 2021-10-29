# create the empty lists
c = []
v = []
b = []
t = []

# perform the task n times
for x in range(10):
    # get the reading
    reading = input("Enter a speed")
    # remove the last letter and convert to int
    speed = int(reading[:-1])
    # get the last letter to make a decision
    reading_type = reading[-1]
    print(speed, reading_type)
    # check to see they type and add speed to correct list
    if reading_type == "c":
        c.append(speed)
    elif reading_type == "v":
        v.append(speed)
    elif reading_type == "b":
        b.append(speed)
    elif reading_type == "t":
        t.append(speed)
# print the results using inbuilt functions
print("Max reading", max(c), "min reading", min(c), "avg", (sum(c) / len(c)))
print("Max reading", max(v), "min reading", min(v), "avg", (sum(v) / len(v)))
print("Max reading", max(b), "min reading", min(b), "avg", (sum(b) / len(b)))
print("Max reading", max(t), "min reading", min(t), "avg", (sum(t) / len(t)))
