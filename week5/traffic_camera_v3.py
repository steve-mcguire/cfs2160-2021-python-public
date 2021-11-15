c = []
v = []
t = []
b = []

for r in range(5):
    reading = input("Please enter a reading")
    speed = int(reading[:-1])
    v_type = reading[-1]
    if v_type == "c":
        c.append(speed)
    elif v_type == "v":
        v.append(speed)
    elif v_type == "b":
        b.append(speed)
    elif v_type == "t":
        t.append(speed)


print("Min",min(c), "Max", max(c), "avg", (sum(c) / len(c)))
print("Min",min(t), "Max", max(t), "avg", (sum(t) / len(t)))
print("Min",min(c), "Max", max(c), "avg", (sum(c) / len(c)))
print("Min",min(c), "Max", max(c), "avg", (sum(c) / len(c)))
