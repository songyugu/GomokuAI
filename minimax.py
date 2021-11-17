"""
This module contains our Minimax AI.
"""

from random import randint
import heuristics as h
import numpy as np


class AI:
    def __init__(self, size, depth=2, pattern_scores=h.PATTERN_SCORES, board_scores=h.BOARD_SCORES_7):
        """
        Initialize the AI with two evalution scoring tables.
        """
        self.p_scores = pattern_scores
        self.b_scores = board_scores
        self.size = size
        self.depth = depth

    def possibles(self, board):
        """
        This function returns a list of possible next slots.
        """
        lst = []
        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] == 0:
                    lst.append((i, j))
        return lst

    def place(self, board, next, player):
        """
        This function returns a new board after player places on next position.
        """
        new_board = np.copy(board)
        x = next[0]
        y = next[1]
        new_board[x][y] = player
        return new_board

    def max_turn(self, board, depth, a, b, player):
        """
        Helper for maximizer.
        """
        if depth == 0:
            return h.board_eval(board, -1, self.p_scores, self.b_scores)
        value = float("-inf")
        for next in self.possibles(board):
            new_board = self.place(board, next, player)
            value = max(value, self.min_turn(
                new_board, depth-1, a, b, -player))
            if value >= b:
                return value
            a = max(a, value)
        return value

    def min_turn(self, board, depth, a, b, player):
        """
        Helper for minimizer.
        """
        if depth == 0:
            return h.board_eval(board, 1, self.p_scores, self.b_scores)
        value = float("inf")
        for next in self.possibles(board):
            new_board = self.place(board, next, player)
            value = min(value, self.max_turn(
                new_board, depth-1, a, b, -player))
            if value <= a:
                return value
            b = min(b, value)
        return value

    def minimax(self, board, player):
        """
        This is the minimax algorithm. Player is either 1 (Black) or -1 (White).
        The player is considered to be maximizier.
        """
        alpha = float("-inf")
        beta = float("inf")
        value = float("-inf")

        nexts = self.possibles(board)

        if not nexts:  # no more available slots
            return (-1, -1)

        next_step = nexts[0]
        # starting from very top MAX, which is the input player
        for i, next in enumerate(nexts):
            new_board = self.place(board, next, player)
            neighbor = self.min_turn(
                new_board, self.depth-1, alpha, beta, -player)
            if neighbor > value:
                value = neighbor
                next_step = next
            alpha = max(alpha, value)
            # print(str(i)+" "+str(value))

        return next_step
