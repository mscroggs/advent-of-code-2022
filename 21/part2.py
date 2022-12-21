import sympy

with open("input") as f:
    data = {}
    for line in f:
        key, value = line.strip().split(": ")
        if " " in value:
            value = value.split(" ")
        else:
            value = int(value)
        data[key] = value

x = sympy.Symbol("x")


def compute(key):
    if key == "humn":
        return x
    d = data[key]
    if isinstance(d, int):
        return d
    if key == "root":
        return compute(d[0]), compute(d[2])
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

a, b = compute("root")
print(sympy.solve(a - b, x)[0])
