x = 1
cycle = 1

print(cycle, x)

add_me = [20, 60, 100, 140, 180, 220]

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
            cycle += 1
            if i == time - 1:
                x += n
            if cycle in add_me:
                total += cycle * x
                print(cycle, x, cycle * x)
print(total)
