with open("input") as f:
    data = [tuple(int(i) for i in line.split(",")) for line in f]

count = 0
for cx, cy, cz in data:
    for dx, dy, dz in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
        if (cx+dx, cy+dy, cz+dz) not in data:
            count += 1
print(count)
