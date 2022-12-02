score = 0

with open("input") as f:
    for line in f:
        ls = line.strip()
        a, x = ls.split()

        if x == "X":  # they win
            if a == "A":
                me = "C"
            if a == "B":
                me = "A"
            if a == "C":
                me = "B"
        elif x == "Y":  # draw
            score += 3
            me = a
        else:  # I win
            score += 6
            if a == "A":
                me = "B"
            if a == "B":
                me = "C"
            if a == "C":
                me = "A"
        if me == "A":
            score += 1
        if me == "B":
            score += 2
        if me == "C":
            score += 3
print(score)
