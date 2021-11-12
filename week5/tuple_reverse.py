# declare the tuple
t = (3, 4, 2, 6, 4, 7, 9)
# declare empty tuple to stored reversed values
r = ()
# loop through reversed tuple using reversed function
for v in reversed(t):
    # get the first element (form reversed tuple)
    # join it with the r tuple
    r = r + (v,)

print(r)