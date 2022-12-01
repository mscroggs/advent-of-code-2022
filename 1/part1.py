maxn = 0

with open("input") as f:
    n = 0
    for line in f:
        if line.strip() == "":
            maxn = max(maxn, n)
            n = 0
        else:
            n += int(line)

maxn = max(maxn, n)
print(maxn)
