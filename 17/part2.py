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
prev = 0
prev2 = 0

# N = 1000000000000
N = 0

for i in range(N):
    # if j == 0:
    #    print("-", i % len(shapes), ymax + 1)
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
        if j == len(dirs):
            print(f"{100 * i // 1000000000000}%", i, i-prev2, ymax, ymax - prev)
            for ploty in range(ymax + 5, ymax - 15, -1):
                print("|" + "".join(["!" if plotx == x and ploty == y else ("#" if (plotx, ploty) in rock else ("@" if (plotx - x, ploty - y) in s else " ")) for plotx in range(7)]) + "|")
            print("-" * 9)
            prev = ymax
            prev2 = i
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
    #if i % 100 == 0:
    #    print(i, f"{100 * i // 1000000000000}%", ymax)

print(ymax + 1)

N = 1748 + (1000000000000 - 1748) % 1750
repeats = (1000000000000 - 1748) // 1750
print(N)

for i in range(N):
    # if j == 0:
    #    print("-", i % len(shapes), ymax + 1)
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
    print(i, f"{100 * i // N}%", ymax + 1)

print(ymax + 1 + 2796 * repeats)

