alph = "abcdefghijklmnopqrstuvwxyz"

with open("input") as f:
    terrain = []
    for i, line in enumerate(f):
        if "S" in line:
            start = (i, line.index("S"))
        if "E" in line:
            end = (i, line.index("E"))
        terrain.append([0 if i == "S" else 25 if i == "E" else alph.index(i) for i in line.strip()])

starts = []
for i, row in enumerate(terrain):
    for j, entry in enumerate(row):
        if entry == 0:
            starts.append((i, j))

mincost = 500
for start in starts:
    costs = [[None for entry in row] for row in terrain]
    costs[start[0]][start[1]] = 0
    new = [start]

    while costs[end[0]][end[1]] is None and len(new) > 0:
        new2 = []
        for n in new:
            pos = []
            if n[0] > 0:
                pos.append((n[0] - 1, n[1]))
            if n[0] < len(costs) - 1:
                pos.append((n[0] + 1, n[1]))
            if n[1] > 0:
                pos.append((n[0], n[1] - 1))
            if n[1] < len(costs[0]) - 1:
                pos.append((n[0], n[1] + 1))
            for p in pos:
                if costs[p[0]][p[1]] is None and terrain[p[0]][p[1]] - terrain[n[0]][n[1]] <= 1:
                    new2.append(p)
                    costs[p[0]][p[1]] = costs[n[0]][n[1]] + 1
        new = new2

    if costs[end[0]][end[1]] is not None:
        mincost = min(mincost, costs[end[0]][end[1]])
print(mincost)
