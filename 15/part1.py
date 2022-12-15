map_data = {}

y = 2000000

with open("input") as f:
    for line in f:
        data = line.split(": ")
        sx = int(data[0].split("x=")[1].split(",")[0])
        sy = int(data[0].split("y=")[1])
        bx = int(data[1].split("x=")[1].split(",")[0])
        by = int(data[1].split("y=")[1])
        if sy == y:
            map_data[sx] = "S"
        if by == y:
            map_data[bx] = "B"
        d = abs(bx-sx) + abs(by-sy)

        if abs(y - sy) <= d:
            j = y - sy
            for i in range(d - abs(j) + 1):
                if sx + i not in map_data:
                    map_data[sx + i] = "#"
                if sx - i not in map_data:
                    map_data[sx - i] = "#"


print(len([i for i in map_data.values() if i != "B"]))
