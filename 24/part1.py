start = None
walls = []
storms = []
stormdirs = []
target = None

with open("input") as f:
    for i, line in enumerate(f):
        for j, c in enumerate(line.strip()):
            if c == ".":
                if start is None:
                    start = (j, i)
                target = (j, i)
            elif c == "#":
                walls.append((j, i))
            else:
                assert c in "<>v^"
                storms.append((j, i))
                stormdirs.append(c)

wall_xy = [
    (min(x for x,y in walls), max(x for x,y in walls)),
    (min(y for x,y in walls), max(y for x,y in walls))]
for x, y in walls:
    assert x in wall_xy[0] or y in wall_xy[1]


mins = 0
possible = [start]
while target not in possible:
    for i, (pos, dir) in enumerate(zip(storms, stormdirs)):
        if dir == ">":
            new_x = pos[0] + 1
            if new_x == wall_xy[0][1]:
                new_x = wall_xy[0][0] + 1
            storms[i] = (new_x, pos[1])
        elif dir == "<":
            new_x = pos[0] - 1
            if new_x == wall_xy[0][0]:
                new_x = wall_xy[0][1] - 1
            storms[i] = (new_x, pos[1])
        elif dir == "v":
            new_y = pos[1] + 1
            if new_y == wall_xy[1][1]:
                new_y = wall_xy[1][0] + 1
            storms[i] = (pos[0], new_y)
        elif dir == "^":
            new_y = pos[1] - 1
            if new_y == wall_xy[1][0]:
                new_y = wall_xy[1][1] - 1
            storms[i] = (pos[0], new_y)
    if (target[0], target[1] - 1) in possible:
        possible = [target]
    else:
        new_possible = []
        for x in range(wall_xy[0][0] + 1, wall_xy[0][1]):
            for y in range(wall_xy[1][0] + 1, wall_xy[1][1]):
                if (x, y) not in storms:
                    if (x, y) in possible or (x-1,y) in possible or (x+1,y) in possible or (x, y-1) in possible or (x,y+1) in possible:
                        new_possible.append((x, y))
        possible = new_possible
    mins += 1
    print(mins, len(possible))

    #print()
    #for y in range(wall_xy[1][0], wall_xy[1][1] + 1):
    #    ls = []
    #    for x in range(wall_xy[0][0], wall_xy[0][1] + 1):
    #        if (x in wall_xy[0] or y in wall_xy[1]) and (x, y) not in [start, target]:
    #            ls.append("#")
    #        elif (x, y) in storms:
    #            if storms.count((x, y)) > 1:
    #                ls.append(f"{storms.count((x, y))}")
    #            else:
    #                ls.append(stormdirs[storms.index((x, y))])
    #        elif (x, y) in possible:
    #            ls.append(".")
    #        else:
    #            ls.append(" ")
    #    print("".join(ls))
    #print()

print(mins)
