from math import gcd

with open("input") as f:
    file = f.read()

monkeys = []
lcm = 1

class Monkey:
    def __init__(self, n, items, operation, factor, true, false):
        self.n = n
        self.items = items
        self.operation = operation
        self.factor = factor
        self.true = true
        self.false = false
        self.inspections = 0

    def look_at_items(self):
        global monkeys, lcm

        self.inspections += len(self.items)

        for i in self.items:
            j = self.operate(i)
            j %= lcm
            if j % self.factor == 0:
                monkeys[self.true].add(j)
            else:
                monkeys[self.false].add(j)
        self.items = []

    def operate(self, n):
        out = self.operation.replace("old", f"{n}")
        return eval(out)

    def add(self, item):
        self.items.append(item)


for monkey in file.split("\n\n"):
    monkey = monkey.split("\n")
    n = int(monkey[0].split(" ")[1].split(":")[0])
    items = [int(i) for i in monkey[1].split(":")[1].split(",")]
    operation = monkey[2].split(" = ")[1]
    factor = int(monkey[3].split(" ")[-1])
    true = int(monkey[4].split(" ")[-1])
    false = int(monkey[5].split(" ")[-1])

    monkeys.append(Monkey(n, items, operation, factor, true, false))

    lcm *= factor

for round in range(10000):
    for m in monkeys:
        m.look_at_items()

values = [m.inspections for m in monkeys]
values.sort()
print(values[-1] * values[-2])
