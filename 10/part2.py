x = 1
xpos = 0
ypos = 0

display = [[" " for _ in range(40)] for _ in range(6)]

total = 0
with open("input") as f:
    for line in f:
        line = line.strip()
        if line == "noop":
            time = 1
            n = 0
        else:
            assert line.startswith("addx ")
            n = int(line[5:])
            time = 2
        for i in range(time):
            xpos += 1
            if xpos >= 40:
                xpos = 0
                ypos += 1
            if i == time - 1:
                x += n
            if abs(x - xpos) <= 1:
                display[ypos][xpos] = "#"

for row in display:
    print("".join(row))
