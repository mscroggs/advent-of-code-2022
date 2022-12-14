cavern = {}

def get_contents(x, y):
    if (x, y) in cavern:
        return cavern[(x, y)]
    return None

max_y = 0

with open("input") as f:
    for line in f:
        ls = line.strip().split(" -> ")
        for start, end in zip(ls[:-1], ls[1:]):
            start = [int(i) for i in start.split(",")]
            end = [int(i) for i in end.split(",")]

            for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
                for j in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                    cavern[(i, j)] = "ROCK"

            max_y = max(start[1], end[1], max_y)

def drop_sand():
    sandpos = (500, 0)

    while True:
        if sandpos[1] > max_y:
            return sandpos
        if get_contents(sandpos[0], sandpos[1] + 1) is None:
            sandpos = (sandpos[0], sandpos[1] + 1)
        elif get_contents(sandpos[0] - 1, sandpos[1] + 1) is None:
            sandpos = (sandpos[0] - 1, sandpos[1] + 1)
        elif get_contents(sandpos[0] + 1, sandpos[1] + 1) is None:
            sandpos = (sandpos[0] + 1, sandpos[1] + 1)
        else:
            return sandpos
n = 0
while True:
    sandpos = drop_sand()
    cavern[sandpos] = "SAND"
    if sandpos[1] > max_y:
        break
    n += 1
print(n)
