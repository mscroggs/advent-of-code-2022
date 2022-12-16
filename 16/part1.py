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

time = 30
rooms = sorted(list(flow.keys()))

def score(done):
    out = 0
    for i, (j, k) in enumerate(done):
        if j == "on":
            out += (time - i - 1) * flow[k]
    return out

best = {}

def best_route(done=None):
    global best
    routes = []
    if done is None:
        pos = "AA"
        done = []
    else:
        pos = done[-1][1]

    if len(done) == time:
        return done

    route = done + [("skip", pos) for i in range(time-len(done))]
    if sum(j for i, j in flow.items() if ("on", i) not in done) == 0:
        return route

    info = (pos, tuple(i for i in rooms if ("on", i) in done), len(done))
    if info in best:
        return done + best[info]

    maxf = score(route)
    if len(done) > 0 and done[-1][0] == "move" and ("on", pos) not in done and flow[pos] > 0:
        r = best_route(done + [("on", pos)])
        s = score(r)
        if s > maxf:
            maxf = s
            route = r
    for i in tunnels[pos]:
        if len(done) >= 3 and done[-1][0] == done[-2][0] == done[-3][0] == "move" and done[-1][1] == done[-3][1] and done[-2][1] == i:
            continue
        r = best_route(done + [("move", i)])
        s = score(r)
        if s > maxf:
            maxf = s
            route = r
    assert route is not None
    best[info] = route[len(done):]
    return route

r = best_route()
print(score(r))
