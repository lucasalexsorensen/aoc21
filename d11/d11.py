import numpy as np

X = np.array([[int(n) for n in l.strip()] for l in open("d11.txt", "r").readlines()])

# part one
total = 0
for step in range(100):
    X += 1
    seen = set()
    while True:
        pairs = np.argwhere(X > 9)
        if len(seen) == len(pairs):
            break

        for r, c in pairs:
            if (r, c) not in seen:
                X[max(0, r - 1) : r + 2, max(0, c - 1) : c + 2] += 1
                seen.add((r, c))
    X[X > 9] = 0
    total += np.count_nonzero(X == 0)
print("Part one result: %d" % total)

# part two
X = np.array([[int(n) for n in l.strip()] for l in open("d11.txt", "r").readlines()])

counter = 0
while True:
    counter += 1
    X += 1
    seen = set()
    while True:
        pairs = np.argwhere(X > 9)
        if len(seen) == len(pairs):
            break

        for r, c in pairs:
            if (r, c) not in seen:
                X[max(0, r - 1) : r + 2, max(0, c - 1) : c + 2] += 1
                seen.add((r, c))
    X[X > 9] = 0
    if np.count_nonzero(X == 0) == X.size:
        break
print("Part two result: %d" % counter)
