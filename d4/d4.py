import re

import numpy as np

lines = open("d4.txt", "r").readlines()

sequence = [int(n) for n in lines[0].split(",")]

boards = []
for i in range(2, len(lines), 6):
    boards.append([[int(n) for n in line.split()] for line in lines[i : i + 5]])
boards = np.array(boards)


def calc_board_score(masks, boards, board_idx, n):
    board = boards[board_idx, :, :]
    mask = masks[board_idx, :, :]
    return n * np.sum(board * ~mask)


# part one
result = None
masks = np.zeros_like(boards).astype(bool)
for s in sequence:
    masks |= boards == s

    col_sum = masks.sum(axis=1)
    row_sum = masks.sum(axis=2)
    board_idx, row_idx = np.where(row_sum == boards.shape[1])
    if board_idx.size > 0:
        result = calc_board_score(masks, boards, board_idx[0], s)
    board_idx, col_idx = np.where(col_sum == boards.shape[2])
    if board_idx.size > 0:
        result = calc_board_score(masks, boards, board_idx[0], s)

    if result:
        print("Part one result:", result)
        break

# part two
masks = np.zeros_like(boards).astype(bool)
prev_completed = set()
for s in sequence:
    masks |= boards == s

    col_sum = masks.sum(axis=1)
    row_sum = masks.sum(axis=2)
    completed = set(
        x[0] for x in np.argwhere((row_sum == boards.shape[1]) | (col_sum == boards.shape[2]))
    )
    if len(completed) >= boards.shape[0]:
        board_idx = list(completed - prev_completed)
        print("Part two result:", calc_board_score(masks, boards, board_idx, s))
        break
    prev_completed = completed.copy()
