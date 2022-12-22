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

for p in path:
    if isinstance(p, int):
        for i in range(p):
            newpos = (pos[0] + dir[0], pos[1] + dir[1])
            if newpos not in mapdata:
                if dir == (1, 0):
                    newpos = (min(x for x, y in mapdata if y == pos[1]), pos[1])
                elif dir == (-1, 0):
                    newpos = (max(x for x, y in mapdata if y == pos[1]), pos[1])
                elif dir == (0, 1):
                    newpos = (pos[0], min(y for x, y in mapdata if x == pos[0]))
                else:
                    assert dir == (0, -1)
                    newpos = (pos[0], max(y for x, y in mapdata if x == pos[0]))
            if mapdata[newpos] == ".":
                pos = newpos
    elif p == "R":
        dir = R[dir]
    elif p == "L":
        dir = L[dir]
    else:
        raise ValueError

facing = {(1, 0): 0, (0, 1): 1, (-1, 0): 2, (0, -1): 3}
print(1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + facing[dir])
