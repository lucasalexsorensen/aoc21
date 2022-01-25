from dataclasses import dataclass
from typing import Tuple

import numpy as np


@dataclass
class Operation:
    name: str
    value: int


def line_to_op(line: str) -> Operation:
    s = line.split(" ")
    return Operation(name=s[0], value=int(s[1]))


ops = [line_to_op(l) for l in open("d2.txt", "r")]

# part one

StateChange = Tuple[int, int]  # (horizontal pos, depth, aim)


def handle_op(op: Operation) -> StateChange:
    if op.name == "forward":
        return (op.value, 0)
    elif op.name == "up":
        return (0, -op.value)
    elif op.name == "down":
        return (0, op.value)


effects = np.array([handle_op(op) for op in ops])
final_state = effects.sum(axis=0)

print("Part one result: %d" % final_state.prod())


# part two
# State = Tuple[int, int, int]
@dataclass
class State:
    pos: int
    depth: int
    aim: int


state = State(pos=0, depth=0, aim=0)


def handle_op2(state: State, op: Operation) -> State:
    if op.name == "forward":
        return State(state.pos + op.value, state.depth + state.aim * op.value, state.aim)
    elif op.name == "up":
        return State(state.pos, state.depth, state.aim - op.value)
    elif op.name == "down":
        return State(state.pos, state.depth, state.aim + op.value)


for op in ops:
    state = handle_op2(state, op)

print("Part two result: %d" % (state.pos * state.depth))
