class MultiItem:
    def __init__(self, ore=0, clay=0, obsidian=0, geode=0):
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode

    def __add__(self, other):
        return MultiItem(
            ore=self.ore + other.ore,
            clay=self.clay + other.clay,
            obsidian=self.obsidian + other.obsidian,
            geode=self.geode + other.geode
        )

    def __sub__(self, other):
        return MultiItem(
            ore=self.ore - other.ore,
            clay=self.clay - other.clay,
            obsidian=self.obsidian - other.obsidian,
            geode=self.geode - other.geode
        )

    def __eq__(self, other):
        return self.ore == other.ore and self.clay == other.clay and self.obsidian == other.obsidian

    def __le__(self, other):
        return self.ore <= other.ore and self.clay <= other.clay and self.obsidian <= other.obsidian and self.geode <= other.geode

    def __lt__(self, other):
        return self.ore < other.ore and self.clay < other.clay and self.obsidian < other.obsidian and self.geode < other.geode

    def __repr__(self):
        return f"ore: {self.ore}; clay: {self.clay}; obsidian: {self.obsidian}; geode: {self.geode}"

options = []
with open("test-input") as f:
    for line in f:
        o = []
        for r in line.strip().split(": ")[1].split(".")[:-1]:
            materials = {}
            target = r.strip().split(" ")[1]
            r = r.split("costs")[1].strip()
            for i in r.split("and"):
                n, item = i.strip().split(" ")
                materials[item] = int(n)
            o.append((MultiItem(**{target: 1}), MultiItem(**materials)))
        assert o[-1][0].geode == 1
        options.append(o[::-1])

T = 24

best = 0
def generate_options(blueprint, maxes, robots=MultiItem(ore=1), inventory=MultiItem(), t=0):
    global best
    if robots.ore > maxes.ore or robots.clay > maxes.clay or robots.obsidian > maxes.obsidian:
        return
    if robots.ore >= blueprint[0][1].ore and robots.clay >= blueprint[0][1].clay and robots.obsidian >= blueprint[0][1].obsidian:
        if robots.ore > blueprint[0][1].ore or robots.clay > blueprint[0][1].clay or robots.obsidian > blueprint[0][1].obsidian:
            return
    if t == 24:
        if inventory.geode > best:
            best = inventory.geode
            print(best)
        return

    if inventory.geode + robots.geode * (24 - t) + (24-t)*(25-t)//2 < best:
       return

    c = False
    for build, cost in blueprint:
        if cost <= inventory:
            generate_options(blueprint, maxes, robots + build, inventory - cost + robots, t+1)
        else:
            c = True
    if c:
        generate_options(blueprint, maxes, robots, inventory + robots, t+1)


result = 0
for i, b in enumerate(options):
    print("==", i, "==")
    best = 0
    maxes = MultiItem(
        ore=max(i.ore for _, i in b),
        clay=max(i.clay for _, i in b),
        obsidian=max(i.obsidian for _, i in b),
    )
    generate_options(b, maxes)
    result += (i + 1) * best

print()
print(result)
