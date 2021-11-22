# 1 = on a leaf, 0 = not on a leaf
input_stream = [1, 1, 1, 0, 1, 0, 1, "t"]
invert = 0
stop = 1
state = invert
step = 0
while state != stop:
    if state == invert:
        if input_stream[step] == 1 and input_stream[step] != "t":
            print("Pick up")
            step += 1
            state = invert

        elif input_stream[step] == 0 and input_stream[step] != "t":
            print("Put down")
            step += 1
            state = invert
        elif input_stream[step] == 1 and input_stream[step] == "t":
            print("Pick up")
            state = stop
        elif input_stream[step] == 0 and input_stream[step] == "t":
            print("Put down")
            state = stop
        print(state)
