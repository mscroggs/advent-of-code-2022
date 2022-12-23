elves = []

with open("input") as f:
    for i, line in enumerate(f):
        for j, c in enumerate(line.strip()):
            if c == "#":
                elves.append((j, i))

directions = [
    # N: (0, -1)
    [[(1, -1), (0, -1), (-1, -1)], (0, -1)],
    # S: (0, 1)
    [[(1, 1), (0, 1), (-1, 1)], (0, 1)],
    # W: (-1, 0)
    [[(-1, 1), (-1, 0), (-1, -1)], (-1, 0)],
    # E: (1, 0)
    [[(1, 1), (1, 0), (1, -1)], (1, 0)],
]
moved = True
N = 0
while moved:
    N += 1
    print(N)
    moved = False
    proposed = []
    for e in elves:
        if all(
            (e[0] + a[0], e[1] + a[1]) not in elves
            for a in [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0, -1)]
        ):
            proposed.append(None)
        else:
            for d in directions:
                for i in d[0]:
                    if (e[0]+i[0], e[1]+i[1]) in elves:
                        break
                else:
                    proposed.append((e[0]+d[1][0], e[1]+d[1][1]))
                    break
            else:
                proposed.append(None)
    for i, p in enumerate(proposed):
        if p is not None and proposed.count(p) == 1:
            elves[i] = p
            moved = True

    directions = directions[1:] + directions[:1]
    assert len(proposed) == len(elves)
    #for y in range(min(y for x, y in elves), 1 + max(y for x, y in elves)):
    #    print("".join(
    #        "#" if (x, y) in elves else "."
    #        for x in range(min(x for x, y in elves), 1 + max(x for x, y in elves))
    #    ))
    #print("-"*30)
    if N == 10:
        break

area = max(x for x, y in elves) + 1 - min(x for x, y in elves)
area *= max(y for x, y in elves) + 1 - min(y for x, y in elves)
print(area - len(elves))
