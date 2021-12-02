import numpy as np
from scipy.fft import fft, ifft, next_fast_len

m = np.array([int(n) for n in open("d1.txt")])

# part one
part_one_result = np.count_nonzero(np.diff(m) > 0)
print("Part one result: %d" % part_one_result)


# part two
kernel = np.array([1, 1, 1])
fast_len = next_fast_len(len(m) + len(kernel) - 1)
m_f = fft(np.pad(m, (0, fast_len - len(m))))
kernel_f = fft(np.pad(kernel, (0, fast_len - len(kernel))))
m_convolved = np.round(ifft(m_f * kernel_f).real[len(kernel) - 1 : len(m)])

part_two_result = np.count_nonzero(np.diff(m_convolved) > 0)
print("Part two result: %d" % part_two_result)
