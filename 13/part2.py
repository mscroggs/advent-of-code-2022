import json

def in_order(ls1, ls2):
    if isinstance(ls1, int) and isinstance(ls2, int):
        if ls1 == ls2:
            return None
        return ls1 < ls2

    if isinstance(ls1, int):
        return in_order([ls1], ls2)
    if isinstance(ls2, int):
        return in_order(ls1, [ls2])

    for i, j in zip(ls1, ls2):
        result = in_order(i, j)
        if result is not None:
            return result
    if len(ls1) == len(ls2):
        return None
    return len(ls1) < len(ls2)


data = []
with open("input") as f:
    for line in f:
        if line.strip() != "":
            data.append(json.loads(line.strip()))

n = 1
for line in data:
    if in_order(line, [[2]]):
        n += 1
m = 2
for line in data:
    if in_order(line, [[6]]):
        m += 1

print(n * m)
