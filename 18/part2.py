from itertools import product

with open("input") as f:
    data = [tuple(int(i) for i in line.split(",")) for line in f]

xmin = min(c[0] for c in data)
xmax = max(c[0] for c in data)
ymin = min(c[1] for c in data)
ymax = max(c[1] for c in data)
zmin = min(c[2] for c in data)
zmax = max(c[2] for c in data)

to_add = []
for x, y, z, in product(range(xmin, xmax + 1), range(ymin, ymax + 1), range(zmin, zmax + 1)):
    if (x, y, z) not in data + to_add:
        changed = True
        pts = [(x, y, z)]
        new_pts = [(x, y, z)]
        outside = False
        while not outside and len(new_pts) > 0:
            new_new_pts = []
            for px, py, pz in new_pts:
                for dx, dy, dz in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
                    if (px + dx, py + dy, pz + dz) not in data + pts + new_new_pts:
                        new_new_pts.append((px + dx, py + dy, pz + dz))
            new_pts = new_new_pts
            pts += new_new_pts

            for x, y, z in new_new_pts:
                if xmin > x or xmax < x or ymin > y or ymax < y or zmin > z or zmax < z:
                    outside = True
                    break
        if not outside:
            to_add += pts
data += to_add

count = 0
for cx, cy, cz in data:
    for dx, dy, dz in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
        if (cx+dx, cy+dy, cz+dz) not in data:
            count += 1
print(count)
