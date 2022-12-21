with open("input") as f:
    data = {}
    for line in f:
        key, value = line.strip().split(": ")
        if " " in value:
            value = value.split(" ")
        else:
            value = int(value)
        data[key] = value

def compute(key):
    d = data[key]
    if isinstance(d, int):
        return d
    if d[1] == "+":
        return compute(d[0]) + compute(d[2])
    if d[1] == "-":
        return compute(d[0]) - compute(d[2])
    if d[1] == "*":
        return compute(d[0]) * compute(d[2])
    if d[1] == "/":
        a = compute(d[0])
        b = compute(d[2])
        if a % b == 0:
            return a // b
        return a / b

    raise ValueError()

print(compute("root"))
