"""
This module contains basic Minimax AI.
"""

from random import randint


def next_move(board, player):
    oldboard = board[1:]
    newboard = [x[1:] for x in oldboard]
    x, y = 0, 0
    while newboard[x][y] != " _":
        x = randint(0, 14)
        y = randint(0, 14)
    return x+1, y+1
