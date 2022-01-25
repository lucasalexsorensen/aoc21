import numpy as np
from scipy import optimize

sequence = np.array([int(n) for n in open("d7.txt", "r").read().split(",")])

# minimize the 1-norm of the positions minus the candidate alignment point (x)
def cost(x):
    return np.linalg.norm((sequence - x), 1)


cost = int(np.round(optimize.minimize(cost, 10).fun))
print("Part one result: %d" % cost)


def cost(x):
    diff = np.abs(sequence - x)
    return np.sum(0.5 * (diff + 1) * diff)


# print()
x_opt = int(np.round(optimize.minimize(cost, 10).x[0]))
print("Part one result: %d" % cost(x_opt))

# cost = int(np.round(optimize.minimize(cost, 10).fun))
