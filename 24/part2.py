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

phase = 0

mins = 0
possible = [start]
while phase < 3:
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
    if phase == 0 and (target[0], target[1] - 1) in possible:
        phase += 1
        possible = [target]
    elif phase == 1 and (start[0], start[1] + 1) in possible:
        phase += 1
        possible = [start]
    elif phase == 2 and (target[0], target[1] - 1) in possible:
        phase += 1
        possible = [target]
    else:
        if phase == 1:
            new_possible = [target]
        else:
            new_possible = [start]
        for x in range(wall_xy[0][0] + 1, wall_xy[0][1]):
            for y in range(wall_xy[1][0] + 1, wall_xy[1][1]):
                if (x, y) not in storms:
                    if (x, y) in possible or (x-1,y) in possible or (x+1,y) in possible or (x, y-1) in possible or (x,y+1) in possible:
                        new_possible.append((x, y))
        possible = new_possible
    mins += 1
    print(mins, len(possible))

print(mins)
