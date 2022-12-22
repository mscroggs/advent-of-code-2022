mapdata = {}
pos = None
dir = (1, 0)

with open("input") as f:
    data = f.read()
    mapinput, pathinput = data.split("\n\n")

for y, line in enumerate(mapinput.split("\n")):
    for x, c in enumerate(line):
        if c == ".":
            mapdata[(x, y)] = "."
            if pos is None:
                pos = (x, y)
        elif c == "#":
            mapdata[(x, y)] = "#"
        else:
            assert c == " "

path = []
n = ""
for c in pathinput.strip():
    if c in "0123456789":
        n += c
    else:
        if n != "":
            path.append(int(n))
        path.append(c)
        n = ""
if n != "":
    path.append(int(n))

R = {(1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0)}
L = {j: i for i, j in R.items()}

edges = [
    (((100, 150), 50, (0, 1)), (100, (50, 100), (1, 0))),
    (((50, 100), 150, (0, 1)), (50, (150, 200), (1, 0))),
    (((0, 50), 200, (0, 1)), ((100, 150), -1, (0, -1))),
    (((50, 100), -1, (0, -1)), (-1, (150, 200), (-1, 0))),
    (((0, 50), 99, (0, -1)), (49, (50, 100), (-1, 0))),
    ((150, (0, 50), (1, 0)), (100, (149, 99), (1, 0))),
    ((49, (0, 50), (-1, 0)), (-1, (149, 99), (-1, 0))),
]

for ee in edges:
    for e in ee:
        if isinstance(e[0], int):
            for i in range(*e[1]):
                assert (e[0], i) not in mapdata
        else:
            for i in range(*e[0]):
                assert (i, e[1]) not in mapdata

def contained(pos, edge):
    for p, e in zip(pos, edge[:2]):
        if isinstance(e, int):
            if p != e:
                return False
        elif not min(e) <= p < max(e):
            return False
    return True

def posmap(pos, edge, newedge):
    if isinstance(edge[0], int):
        i = abs(pos[1] - edge[1][0])
    else:
        i = abs(pos[0] - edge[0][0])
    newpos = []
    for p, e, d in zip(pos, newedge[:2], newedge[2]):
        if isinstance(e, int):
            newpos.append(e - d)
        elif e[0] < e[1]:
            newpos.append(e[0] + i)
        else:
            newpos.append(e[0] - i)
    return tuple(newpos), (-newedge[2][0], -newedge[2][1])

positions = [pos]

import matplotlib.pylab as plt

for p in path:
    if isinstance(p, int):
        for i in range(p):
            newpos = (pos[0] + dir[0], pos[1] + dir[1])
            newdir = dir
            ppp = False
            if newpos not in mapdata:
                ppp = True
                for e in edges:
                    for a, b in [e, e[::-1]]:
                        if contained(newpos, a):
                            newpos, newdir = posmap(newpos, a, b)
                            break
                    else:
                        continue
                    break
                else:
                    raise ValueError
            if mapdata[newpos] == ".":
                pos = newpos
                positions.append(pos)
                dir = newdir
    elif p == "R":
        dir = R[dir]
    elif p == "L":
        dir = L[dir]
    else:
        raise ValueError

facing = {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}
print(1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + facing[dir])
