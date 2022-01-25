from collections import Counter
from dataclasses import dataclass


# part one
@dataclass
class Fish:
    timer: int


sequence = [int(n) for n in open("d6.txt", "r").read().split(",")]
state = [Fish(timer=n) for n in sequence]
for epoch in range(80):

    new_fish = []
    for fish in state:
        if fish.timer == 0:
            fish.timer = 6
            new_fish.append(Fish(timer=8))
        else:
            fish.timer -= 1
    state += new_fish

print("Part one result: %d" % len(state))


# part two
state = Counter(sequence)
for day in range(256):
    # progress age of all fish
    for i in range(9):
        state[i - 1] = state[i]

    # spawn new fish
    state[8] = state[-1]

    # reset fish
    state[6] += state[-1]
    state[-1] = 0
print("Part two result: %d" % sum(state.values()))
