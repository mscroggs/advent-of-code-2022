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

def score(done):
    return sum(done.values())

best = {}

def best_route(pos="AA", pos2="AA", t=0, done=None):
    global best
    routes = []
    if done is None:
        done = {}

    if t == time:
        return done

    on = tuple(sorted(list(done.keys())))

    if sum(j for i, j in flow.items() if i not in on) == 0:
        return done

    info = (pos, pos2, on, t)
    if info in best:
        d = done.copy()
        d.update(best[info])
        return d

    maxf = score(done)
    route = done

    moves = []
    if pos not in on and flow[pos] > 0:
        moves.append(({pos: flow[pos] * (time - t - 1)}, pos))
    for i in tunnels[pos]:
        moves.append(({}, i))
    moves2 = []
    if pos2 not in on and flow[pos2] > 0:
        moves2.append(({pos2: flow[pos2] * (time - t - 1)}, pos2))
    for i in tunnels[pos2]:
        moves2.append(({}, i))

    for m in moves:
        for m2 in moves2:
            if m[0] != "on" or m != m2:
                d = done.copy()
                d.update(m[0])
                d.update(m2[0])
                r = best_route(m[1], m2[1], t + 1, d)
                s = score(r)
                if s > maxf:
                    maxf = s
                    route = r

    if info in best:
        A = {i: j for i, j in route.items() if i not in done}
        if A != best[info]:
            from IPython import embed; embed()()

    best[info] = {i: j for i, j in route.items() if i not in done}
    return route

r = best_route()
print(score(r))
