import numpy as np

lines = []
for l in open("d5.txt", "r"):
    l = l.replace("\n", "")
    lines.append([[int(n) for n in p.split(",")] for p in l.split(" -> ")])
lines = np.array(lines)  # (N, X, Y) = (500, 2, 2)

hv_lines = lines[np.squeeze((np.diff(lines, axis=1) == 0).sum(axis=2) >= 1)]
grid = np.zeros(shape=(1000, 1000), dtype="int32")

for line in hv_lines:
    x1, x2 = line[:, 0]
    y1, y2 = line[:, 1]
    s_x = 1 if x1 <= x2 else -1
    s_y = 1 if y1 <= y2 else -1
    indices = tuple(
        [
            np.arange(y1, y2 + s_y, step=s_y),
            np.arange(x1, x2 + s_x, step=s_x),
        ]
    )
    grid[indices] += 1

print("Part one result:", np.sum(grid >= 2))


grid = np.zeros(shape=(1000, 1000), dtype="int32")
for line in lines:
    x1, x2 = line[:, 0]
    y1, y2 = line[:, 1]
    s_x = 1 if x1 <= x2 else -1
    s_y = 1 if y1 <= y2 else -1
    indices = tuple(
        [
            np.arange(y1, y2 + s_y, step=s_y),
            np.arange(x1, x2 + s_x, step=s_x),
        ]
    )
    grid[indices] += 1


print("Part two result:", np.sum(grid >= 2))
