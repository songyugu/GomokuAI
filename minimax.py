"""
This module contains basic Minimax AI.
"""

from random import randint


def next_move(board, player):

    x, y = 0, 0
    while board[x][y] != 0:
        x = randint(0, 14)
        y = randint(0, 14)
    return x, y
