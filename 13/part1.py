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


count = 0
with open("input") as f:
    lists = f.read().split("\n\n")
    for i, l in enumerate(lists):
        data0 = json.loads(l.split("\n")[0])
        data1 = json.loads(l.split("\n")[1])
        if in_order(data0, data1):
            count += i + 1
print(count)
