total = 300470

split = 10

tenth = total / split

start = 0
end = tenth - 1

total = 0
for x in range(split):
    print(round(start), " ", round(end))
    start += tenth
    end += tenth