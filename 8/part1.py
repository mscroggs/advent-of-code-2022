import numpy as np

with open("input") as f:
    trees = np.array([[int(i) for i in line.strip()] for line in f])

def mymax(ls):
    if len(ls) == 0:
        return -1
    return max(ls)

count = 0
for i, row in enumerate(trees):
    for j, tree in enumerate(row):
        if tree > mymax(row[:j]) or tree > mymax(row[j+1:]) or tree > mymax(trees[:i, j]) or tree > mymax(trees[i+1:, j]):
            count += 1
print(count)
