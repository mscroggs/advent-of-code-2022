elves = []

with open("input") as f:
    for i, line in enumerate(f):
        for j, c in enumerate(line.strip()):
            if c == "#":
                elves.append((i, j))

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

adjacent = [i for i, e in enumerate(elves) if any(
    (e[0] + a[0], e[1] + a[1]) in elves
    for a in [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0, -1)]
)]

moved = [i for i in adjacent]
N = 0
while moved:
    N += 1
    count = 0
    new_moved = []
    proposed = {}
    for i in adjacent:
        e = elves[i]
        for d in directions:
            for dd in d[0]:
                if (e[0]+dd[0], e[1]+dd[1]) in elves:
                    break
            else:
                proposed[i] = (e[0]+d[1][0], e[1]+d[1][1])
                break
    pv = list(proposed.values())
    for i, p in proposed.items():
        if p is not None and pv.count(p) == 1:
            elves[i] = p
            new_moved.append(i)

    adjacent = [i for i in adjacent if any(
        (elves[i][0] + a[0], elves[i][1] + a[1]) in elves
        for a in [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0, -1)]
    )]
    adjacent += [
        i for i in new_moved if i not in adjacent and any(
            (elves[i][0] + a[0], elves[i][1] + a[1]) in elves
            for a in [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0, -1)]
        )
    ]
    me = [elves[i] for i in new_moved]
    adjacent += [
        i for i, e in enumerate(elves) if i not in adjacent and any(
            (e[0] + a[0], e[1] + a[1]) in me
            for a in [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0, -1)]
        )
    ]

    adjacent = [i for i, e in enumerate(elves) if any(
        (e[0] + a[0], e[1] + a[1]) in elves
        for a in [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0, -1)]
    )]

    print(N, len(adjacent))
    moved = new_moved

    directions = directions[1:] + directions[:1]

    #for y in range(min(y for x, y in elves), 1 + max(y for x, y in elves)):
    #    print("".join(
    #        "#" if (x, y) in elves else "."
    #        for x in range(min(x for x, y in elves), 1 + max(x for x, y in elves))
    #    ))
    #print("-"*30)
    #if N >= 25:
    #    break

print(N)
