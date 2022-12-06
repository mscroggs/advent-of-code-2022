with open("input") as f:
    data = f.read()

n = 14

for i, d in enumerate(data):
    c = [data[i+j] for j in range(n)]
    for j in c:
        if c.count(j) > 1:
            break
    else:
        print(i + n)
        break
