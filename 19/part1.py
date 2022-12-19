items = ["ore", "clay", "obsidian"]

options = []
with open("input") as f:
    for line in f:
        o = {"geode": None}
        for r in line.strip().split(": ")[1].split(".")[:-1]:
            materials = {i: 0 for i in items}
            target = r.strip().split(" ")[1]
            r = r.split("costs")[1].strip()
            for i in r.split("and"):
                n, item = i.strip().split(" ")
                materials[item] = int(n)
            o[target] = materials
        options.append(o)

T = 24

best = 0
found = {i: {} for i in range(T)}
def generate_options(blueprint, maxes, robots={i: 1 if i == "ore" else 0 for i in items}, inventory={i: 0 for i in items}, t=0, score=0):
    global best
    global found
    if t == T:
        if score > best:
            best = score
            print(score)
        return score

    if score + (T-t)*(T+1-t)//2 < best:
        return 0

    key = tuple(robots.values())
    key2 = tuple(inventory.values())
    if key not in found[t]:
        found[t][key] = {}
    if key2 in found[t][key]:
        return found[t][key][key2] + score

    c = False
    result = None
    for build, cost in blueprint.items():
        if build == "geode" or robots[build] < maxes[build]:
            if all(cost[i] <= inventory[i] for i in items):
                if build == "geode":
                    r = generate_options(blueprint, maxes, {i: robots[i] + 1 if i == build else robots[i] for i in items}, {i: inventory[i] - cost[i] + robots[i] for i in items}, t+1, score + (T-t-1))
                else:
                    r = generate_options(blueprint, maxes, {i: robots[i] + 1 if i == build else robots[i] for i in items}, {i: inventory[i] - cost[i] + robots[i] for i in items}, t+1, score)
                if r is not None:
                    if result is None:
                        result = r
                    result = max(result, r)
            else:
                c = True
    if c:
        r = generate_options(blueprint, maxes, robots, {i: inventory[i] + robots[i] for i in items}, t+1, score)
        if r is not None:
            if result is None:
                result = r
            result = max(result, r)
    if result is not None:
        found[t][key][key2] = result - score
    return result


result = 0
for n, b in enumerate(options):
    print("==", n, "==")
    best = 0
    found = {i: {} for i in range(T)}
    maxes = {i: max(m[i] for m in b.values()) for i in items}
    generate_options(b, maxes)
    result += (n + 1) * best

print()
print(result)
