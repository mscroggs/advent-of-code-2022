alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

bags = []
with open("input") as f:
    for line in f:
        ls = line.strip()
        bags.append(ls)

out = 0
for i, j, k in zip(bags[::3], bags[1::3], bags[2::3]):
    for n, c in enumerate(alpha):
        if c in i and c in j and c in k:
            out += n + 1
print(out)
