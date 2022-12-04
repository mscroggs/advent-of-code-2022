count = 0
with open("input") as f:
    for line in f:
        a, b = line.strip().split(",")
        a0, a1 = [int(i) for i in a.split("-")]
        b0, b1 = [int(i) for i in b.split("-")]
        if b0 <= a0 <= b1 or a0 <= b0 <= a1:
            count += 1

print(count)
