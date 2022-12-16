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
rooms = sorted(list(flow.keys()))

def score(done, done2):
    out = 0
    for i, (j, k) in enumerate(done):
        if j == "on":
            out += (time - i - 1) * flow[k]
    for i, (j, k) in enumerate(done2):
        if j == "on":
            out += (time - i - 1) * flow[k]
    return out

best = {}

def best_route(done=None, done2=None):
    global best
    routes = []
    if done is None:
        pos = "AA"
        pos2 = "AA"
        done = []
        done2 = []
    else:
        pos = done[-1][1]
        pos2 = done2[-1][1]

    if len(done) == time:
        return done, done2

    on = tuple(i for i in rooms if ("on", i) in done + done2)

    route = done + [("skip", pos) for i in range(time-len(done))], done2 + [("skip", pos2) for i in range(time-len(done2))]
    if sum(j for i, j in flow.items() if i not in on) == 0:
        return route

    info = (pos, pos2, on, len(done))
    if info in best:
        return done + best[info][0], done2 + best[info][1]

    maxf = score(*route)

    moves = []
    if len(done) > 0 and pos not in on and flow[pos] > 0:
        moves.append(("on", pos))
    for i in tunnels[pos]:
        if len(done) >= 3 and done[-1][0] == done[-2][0] == done[-3][0] == "move" and done[-1][1] == done[-3][1] and done[-2][1] == i:
            continue
        moves.append(("move", i))
    moves2 = []
    if len(done2) > 0 and pos2 not in on and flow[pos2] > 0:
        moves2.append(("on", pos2))
    for i in tunnels[pos2]:
        if len(done2) >= 3 and done2[-1][0] == done2[-2][0] == done2[-3][0] == "move" and done2[-1][1] == done2[-3][1] and done2[-2][1] == i:
            continue
        moves2.append(("move", i))

    for m in moves:
        for m2 in moves2:
            if m[0] != "on" or m != m2:
                r, r2 = best_route(done + [m], done2 + [m2])
                s = score(r, r2)
                if s > maxf:
                    maxf = s
                    route = r, r2
    best[info] = (route[0][len(done):], route[1][len(done):])
    return route

r = best_route()
print(score(*r))
