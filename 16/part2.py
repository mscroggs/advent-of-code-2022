flow = {}
tunnels = {}

with open("input") as f:
    for line in f:
        valve = line.split(" ")[1]
        flow[valve] = int(line.split("=")[1].split(";")[0])
        part = line.strip().split("to valve")[1]
        if part.startswith("s"):
            part = part[1:]
        part = part[1:]
        tunnels[valve] = part.split(", ")

time = 26

best = {}

def best_route(pos="AA", pos2="AA", t=0, on=None, score=0):
    global best
    if on is None:
        on = []

    if t == time:
        return score

    if sum(j for i, j in flow.items() if i not in on) == 0:
        return score

    info = (pos, pos2, tuple(sorted(on)), t)
    if info in best:
        return score + best[info]

    moves = []
    if pos not in on and flow[pos] > 0:
        moves.append(([pos], flow[pos] * (time - t - 1), pos))
    for i in tunnels[pos]:
        moves.append(([], 0, i))
    moves2 = []
    if pos2 not in on and flow[pos2] > 0:
        moves2.append(([pos2], flow[pos2] * (time - t - 1), pos2))
    for i in tunnels[pos2]:
        moves2.append(([], 0, i))

    max_s = -1

    for m in moves:
        for m2 in moves2:
            if len(m[0]) == len(m2[0]) == 1 and m[0][0] == m2[0][0]:
                continue
            max_s = max(max_s, best_route(m[2], m2[2], t + 1, on + m[0] + m2[0], score + m[1] + m2[1]))

    best[info] = max_s - score
    return max_s

print(best_route())
