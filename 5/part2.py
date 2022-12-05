with open("input") as f:
    a, b = f.read().split("\n\n")

stacks = {i: [] for i in range(1, 10)}
for row in a.split("\n")[-2::-1]:
    for i, j in enumerate(range(1, len(row), 4)):
        if row[j] != " ":
            stacks[i+1].append(row[j])

for line in b.split("\n"):
    if line != "":
        n = int(line.split("move ")[1].split(" from")[0])
        start = int(line.split("from ")[1].split(" to")[0])
        end = int(line.split("to ")[1])
        stacks[end] += stacks[start][-n:]
        stacks[start] = stacks[start][:-n]

print("".join(i[-1] for i in stacks.values()))
