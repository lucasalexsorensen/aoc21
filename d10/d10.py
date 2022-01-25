import numpy as np

# cto = {")": "(", "]": "[", "}": "{", ">": "<"}
# points = {")": 3, "]": 57, "}": 1197, ">": 25137}
# s = 0

# vocab = {"(": 5, ")": 7, "[": 11, "]": 13, "{": 17, "}": 19, "<": 23, ">": 29}
vocab = {"(": 5, ")": -5, "[": 11, "]": -11, "{": 17, "}": -17, "<": 23, ">": -23}

line = open("test.txt", "r").readlines()[0].strip()

x = np.array([vocab[c] for c in line])
counts, bins = np.histogram(x)
print(counts, bins)

# for line in open("d10.txt", "r").readlines():
#     stack = []
#     for char in line.strip():
#         if char in cto.values():
#             stack.append(char)
#         elif not stack or stack.pop() != cto[char]:
#             s += points[char]
#             break
