"""
This module contains basic Minimax AI.
"""

from random import randint
import heuristics as h
import numpy as np


def availables(board, player):
    """
    This function returns a list of possible slots for the given player to play.
    """
    lst = []
    for i in range(15):
        for j in range(15):
            if board[i][j] == 0:
                lst.append((i, j))
    return lst


def place(board, next, player):
    """
    This function returns a new board after player places on next position.
    """
    new_board = np.copy(board)
    x = next[0]
    y = next[1]
    new_board[x][y] = player
    return new_board


def max_turn(board, curr_depth, depth, a, b):
    if curr_depth == depth:
        return h.board_eval(board, -1)
    value = float("-inf")
    for next in availables(board, -1):
        new_board = place(board, next, -1)
        value = max(value, min_turn(new_board, curr_depth+1, depth, a, b))
        if value >= b:
            return value
        a = max(a, value)
    return value


def min_turn(board, curr_depth, depth, a, b):
    if curr_depth == depth:
        return h.board_eval(board, 1)
    value = float("inf")
    for next in availables(board, 1):
        new_board = place(board, next, 1)
        value = min(value, max_turn(new_board, curr_depth+1, depth, a, b))
        if value <= a:
            return value
        b = min(b, value)
    return value


def minimax(board, player, depth=2):
    nexts = availables(board, player)
    next_step = nexts[0]
    alpha = float("-inf")
    beta = float("inf")
    value = float("-inf")
    if not nexts:
        print("Tie.")
        return
    for i, next in enumerate(nexts):
        new_board = place(board, next, -1)
        neighbor = min_turn(new_board, 1, depth, alpha, beta)
        if neighbor > value:
            value = neighbor
            next_step = next
        alpha = max(alpha, value)
        # print(str(i)+" "+str(value))
    return next_step
