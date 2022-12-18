with open("input") as f:
    dirs = [i for i in f.read().strip()]

shapes = [
    [(0,0), (1,0), (2,0), (3,0)],
    [(1,0), (0,1), (1,1), (2,1), (1,2)],
    [(0,0), (1,0), (2,0), (2,1), (2,2)],
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (1,0), (0,1), (1,1)],
]

rock = []
ymax = -1
j = 0
for i in range(2022):
    s = shapes[i % len(shapes)]
    y = ymax + 4
    x = 2
    while True:
        if dirs[j] == ">":
            if max(x + sx for sx, sy in s) < 6:
                for sx, sy in s:
                    if (x + sx + 1, y + sy) in rock:
                        break
                else:
                    x += 1
        else:
            if x > 0:
                for sx, sy in s:
                    if (x + sx - 1, y + sy) in rock:
                        break
                else:
                    x -= 1
        j += 1
        j %= len(dirs)

        if y == 0:
            break

        for sx, sy in s:
            if (x + sx, y + sy - 1) in rock:
                break
        else:
            y -= 1
            continue
        break
    for sx, sy in s:
        rock.append((x + sx, y + sy))

    ymax = max(ry for rx, ry in rock)

    #for ploty in range(ymax + 5, -1, -1):
    #    print("|" + "".join(["#" if (plotx, ploty) in rock else " " for plotx in range(7)]) + "|")
    #print("-" * 9)

print(ymax + 1)
