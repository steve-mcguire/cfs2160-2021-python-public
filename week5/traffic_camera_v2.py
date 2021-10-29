c = []
v = []
t = []
b = []

for x in range(5):
    reading = input("Enter reading")
    speed = int(reading[:-1])
    vehicle_type = reading[-1]
    if vehicle_type == "c":
        c.append(speed)
    elif vehicle_type == "v":
        v.append(speed)
    elif vehicle_type == "b":
        b.append(speed)
    elif vehicle_type == "t":
        t.append(speed)
    else:
        print("invalid reading")

for v_type in [c, v, b, t]:
    print("Min", min(v_type), "max", max(v_type),
          "avg", (sum(v_type) / len(v_type)))

