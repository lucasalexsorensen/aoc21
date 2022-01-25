from functools import reduce

import numpy as np

x = np.array([[int(n) for n in l if n != "\n"] for l in open("d3.txt")])

# part one
bin_seq_to_dec = lambda seq: reduce(lambda prev, curr: 2 * prev + curr, seq)
gamma = bin_seq_to_dec(np.round(x.mean(axis=0) > 0.5))
epsilon = bin_seq_to_dec(np.round(x.mean(axis=0) < 0.5))
print("Part one result: %d" % int(np.round(gamma * epsilon)))

# part two
def criteria(x, mode):
    values, counts = np.unique(x, return_counts=True)
    # if len(counts) == 2 and counts[0] == counts[1]:
    #     return 1 if mode == "most" else 0
    if mode == "most":
        return values[np.argmax(counts)]
    elif mode == "least":
        return values[np.argmin(counts)]


oxygen = x.copy()


def decode_report(x, mode):
    for col_idx in range(x.shape[1]):
        col = x[:, col_idx]
        x = x[col == criteria(col, mode)]
        if len(x) == 1:
            break
    return x[0]


oxygen = decode_report(x.copy(), "most")
co2 = decode_report(x.copy(), "least")

print("Part two result: %d" % (bin_seq_to_dec(oxygen) * bin_seq_to_dec(co2)))
