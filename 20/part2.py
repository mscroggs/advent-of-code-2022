key = 811589153

with open("input") as f:
    numbers = [int(line) for line in f]

def mod(a, b):
    if a == 0:
        return 0
    if a % b == 0:
        return b
    return a % b

numbers = [n * key for n in numbers]

permutation = [i for i, _ in enumerate(numbers)]

for _ in range(10):
    print(_)
    for i, j in enumerate(numbers):
        pos = permutation.index(i)
        new_pos = permutation.index(i) + j % (len(permutation) - 1)
        while new_pos <= 0:
            new_pos += len(permutation) - 1
        while new_pos >= len(permutation):
            new_pos -= len(permutation) - 1
        permutation = permutation[:pos] + permutation[pos + 1:]
        permutation = permutation[:new_pos] + [i] + permutation[new_pos:]

numbers = [numbers[p] for p in permutation]
assert numbers.count(0) == 1
ind0 = numbers.index(0)
print(numbers[(ind0 + 1000) % len(permutation)] + numbers[(ind0 + 2000) % len(permutation)] + numbers[(ind0 + 3000) % len(permutation)])
