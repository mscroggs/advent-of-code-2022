alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

out = 0
with open("input") as f:
    for line in f:
        ls = line.strip()
        n = len(ls) // 2
        for i, c in enumerate(alpha):
            if c in ls[:n] and c in ls[n:]:
                out += i + 1
print(out)
