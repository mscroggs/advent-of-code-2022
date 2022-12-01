ns = []

with open("input") as f:
    n = 0
    for line in f:
        if line.strip() == "":
            ns.append(n)
            n = 0
        else:
            n += int(line)

ns.append(n)

n = 0
for _ in range(3):
    n += max(ns)
    ns.remove(max(ns))
print(n)
