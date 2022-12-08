import numpy as np

with open("input") as f:
    trees = np.array([[int(i) for i in line.strip()] for line in f])

def mymax(ls):
    if len(ls) == 0:
        return -1
    return max(ls)

answer = 0
for i, row in enumerate(trees):
    for j, tree in enumerate(row):
        score = 1
        for ls in [row[:j][::-1], row[j+1:], trees[:i,j][::-1], trees[i+1:, j]]:
            count = 0
            for a in ls:
                count += 1
                if a >= tree:
                    break
            score *= count
        answer = max(answer, score)
print(answer)
