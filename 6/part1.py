with open("input") as f:
    data = f.read()

for i, d in enumerate(data):
    c = [data[i], data[i+1], data[i+2], data[i+3]]
    for j in c:
        if c.count(j) > 1:
            break
    else:
        print(i + 4)
        break
