h = (0, 0)
t = (0, 0)
positions = {t}

with open("input") as f:
    for line in f:
        d, l = line.strip().split()
        for _ in range(int(l)):
            if d == "R":
                h = (h[0] + 1, h[1])
            elif d == "L":
                h = (h[0] - 1, h[1])
            elif d == "U":
                h = (h[0], h[1] + 1)
            elif d == "D":
                h = (h[0], h[1] - 1)
            else:
                raise ValueError

            if max(abs(h[0]-t[0]), abs(h[1]-t[1])) > 1:
                if h[0] == t[0] or (h[0] != t[0] and h[1] != t[1]):
                    if h[1] > t[1]:
                        t = (t[0], t[1] + 1)
                    else:
                        t = (t[0], t[1] - 1)
                if h[1] == t[1] or (h[0] != t[0] and h[1] != t[1]):
                    if h[0] > t[0]:
                        t = (t[0] + 1, t[1])
                    else:
                        t = (t[0] - 1, t[1])
            positions.add(t)
print(len(positions))
