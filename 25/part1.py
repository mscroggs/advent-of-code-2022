def to_decimal(a):
    n = 0
    for i, j in enumerate(a[::-1]):
        if j == "=":
            n += -2 * 5 ** i
        elif j == "-":
            n += -1 * 5 ** i
        else:
            n += int(j) * 5 ** i
    return n

def from_decimal(n):
    out = ""
    digits = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}

    while n > 0:
        i = n % 5

        if i > 2:
            i -= 5
        out = digits[i] + out
        n -= i
        assert n % 5 == 0

        n //= 5
    return out

total = 0
with open("input") as f:
    for line in f:
        total += to_decimal(line.strip())

print(from_decimal(total))

