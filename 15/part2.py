pmax = 4000000

possibilities = {j: [(0, pmax)] for j in range(pmax + 1)}
sensors = []
beacons = []

def print_map():
    ls = [["#" for x in range(pmax + 1)] for y in range(pmax + 1)]
    for x in range(pmax + 1):
        for a, b in possibilities[x]:
            for y in range(a, b + 1):
                ls[y][x] = " "
    for x, y in beacons:
        if 0 <= x <= pmax and 0 <= y <= pmax:
            ls[y][x] = "B"
    for x, y in sensors:
        if 0 <= x <= pmax and 0 <= y <= pmax:
            ls[y][x] = "S"
    for line in ls:
        print("".join(line))


with open("input") as f:
    for line in f:
        data = line.split(": ")
        sx = int(data[0].split("x=")[1].split(",")[0])
        sy = int(data[0].split("y=")[1])
        bx = int(data[1].split("x=")[1].split(",")[0])
        by = int(data[1].split("y=")[1])
        d = abs(bx-sx) + abs(by-sy)
        sensors.append((sx, sy))
        beacons.append((bx, by))

        for px in range(max(0, sx-d), min(pmax, sx + d) + 1):
            k = d - abs(px - sx)
            ymin = sy - k
            ymax = sy + k
            new_poss = []

            i = 0
            while i < len(possibilities[px]) and possibilities[px][i][1] < ymin:
                new_poss.append(possibilities[px][i])
                i += 1
            if i < len(possibilities[px]):
                if possibilities[px][i][0] < ymin:
                    new_poss.append((possibilities[px][i][0], ymin - 1))
            while i < len(possibilities[px]) and possibilities[px][i][1] < ymax:
                i += 1
            if i < len(possibilities[px]) and possibilities[px][i][0] < ymax:
                if possibilities[px][i][1] > ymax:
                    new_poss.append((ymax + 1, possibilities[px][i][1]))
                i += 1
            new_poss += possibilities[px][i:]
            possibilities[px] = new_poss
        print(line.strip())

points = [(i, j) for i, d in possibilities.items() for a, b in d for j in range(a, b + 1)]

assert len(points) == 1

print(points[0][0] * 4000000 + points[0][1])
