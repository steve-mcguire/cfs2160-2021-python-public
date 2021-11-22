c = []
v = []
b = []
t = []


def print_stats(l):
    return "Total", len(l), "Max", max(l), "Min", min(l), "AVG", sum(l) / len(l)


for x in range(5):
    reading = input("Enter a reading")
    speed = int(reading[:-1])
    v_type = reading[-1:]
    if v_type == "c":
        c.append(speed)
    elif v_type == "b":
        b.append(speed)
    elif v_type == "v":
        v.append(speed)
    elif v_type == "t":
        t.append(speed)

'''print("Max", max(c), "Min", min(c), "AVG", sum(c) / len(c))
print("Max", max(v), "Min", min(v), "AVG", sum(v) / len(v))
print("Max", max(c), "Min", min(c), "AVG", sum(c) / len(c))
print("Max", max(c), "Min", min(c), "AVG", sum(c) / len(c))'''

print(print_stats(c))
print(print_stats(v))
print(print_stats(b))
print(print_stats(t))