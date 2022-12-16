flow = {}
tunnels = {}

with open("test-input") as f:
    for line in f:
        print(line)
        valve = line.split(" ")[1]
        flow[valve] = int(line.split("=")[1].split(";")[0])
        part = line.strip().split("to valve")[1]
        if part.startswith("s"):
            part = part[1:]
        part = part[1:]
        tunnels[valve] = part.split(", ")

print(flow)
print(tunnels)

def score(done):
    out = 0
    for i, (j, k) in enumerate(done):
        if j == "on":
            out += (30 - i - 1) * flow[k]
    return out

maxf = 0

def all_routes(done=None):
    global maxf

    routes = []
    if done is None:
        done = []
        pos = "AA"
    else:
        pos = done[-1][1]

    if len(done) == 30:
        s = score(done)
        if s > maxf:
            maxf = s
            print(done)
            print(maxf)
        return

    routes = []
    if len(done) > 0 and done[-1][0] == "move" and ("on", pos) not in done and flow[pos] > 0:
        all_routes(done + [("on", pos)])
    movesonly = [j for i, j in done if i == "move"]
    for i in tunnels[pos]:
        if len(movesonly) >= 3 and movesonly[-1] == movesonly[-3] and movesonly[-2] == i:
            continue
        all_routes(done + [("move", i)])

for r in all_routes():
    print(r)
