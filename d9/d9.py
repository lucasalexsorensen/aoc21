import numpy as np
from scipy.ndimage import label

raw = np.array([[int(n) for n in line.strip()] for line in open("d9.txt", "r")])
m = 9 * np.ones(2 + np.array(raw.shape), dtype="int32")
m[1:-1, 1:-1] = raw

diff_right = np.diff(m, axis=1)[1:-1, :-1]
diff_left = np.flip(np.diff(np.flip(m, axis=1), axis=1), axis=1)[1:-1, 1:]
diff_up = np.diff(m, axis=0)[:-1, 1:-1]
diff_down = np.flip(np.diff(np.flip(m, axis=0), axis=0), axis=0)[1:, 1:-1]

diff_union = (diff_right < 0) & (diff_left < 0) & (diff_up < 0) & (diff_down < 0)

print("Part one result:", np.sum(1 + raw[diff_union]))


connected, _ = label(raw < 9)
c = np.bincount(connected[connected > 0].reshape(1, -1).flatten())
print("Part two result: %d" % np.prod(sorted(c, reverse=True)[:3]))
