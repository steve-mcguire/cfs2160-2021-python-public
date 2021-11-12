permitted_types = ["c", "v", "b", "t"]
readings = []
errors = []

while True:
    reading = input("Enter a reading: ")
    if reading == "end":
        break
    elif reading[-1] in permitted_types:
        readings.append(reading)
    else:
        print("invalid reading")
        errors.append(reading)

for v in permitted_types:
    # python generator expression, really cool stuff, like an inline for loop
    sub_list = [int(i[:-1]) for i in readings if v in i]
    print(v, "Number of vehicles", len(sub_list), "Min", min(sub_list), "Max", max(sub_list), "Avg",
          round(sum(sub_list) / len(sub_list), 2))

print(len(errors), "errors entered")

