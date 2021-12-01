"""
This module contains game board evaluation functions and default evaluabtion score tables.
"""

import numpy as np
from numpy.core.arrayprint import str_format
import regex as re

BOARD_SCORES_15 = [[0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0],
                   [0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0],
                   [0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0],
                   [0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0, 0, 0],
                   [0, 0, 0, 0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2, 0, 0, 0],
                   [0, 0, 0, 0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2, 0, 0, 0],
                   [0, 0, 0, 0.2, 0.4, 0.6, 0.8, 0.8, 0.8, 0.6, 0.4, 0.2, 0, 0, 0],
                   [0, 0, 0, 0.2, 0.4, 0.6, 0.8, 1.0, 0.8, 0.6, 0.4, 0.2, 0, 0, 0],
                   [0, 0, 0, 0.2, 0.4, 0.6, 0.8, 0.8, 0.8, 0.6, 0.4, 0.2, 0, 0, 0],
                   [0, 0, 0, 0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2, 0, 0, 0],
                   [0, 0, 0, 0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2, 0, 0, 0],
                   [0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0, 0, 0],
                   [0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0],
                   [0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0],
                   [0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0]]

BOARD_SCORES_9 = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, 0.0, 0.3, 0.3, 0.3, 0.3, 0.3, 0.0, 0.0],
                  [0.0, 0.0, 0.3, 0.6, 0.6, 0.6, 0.3, 0.0, 0.0],
                  [0.0, 0.0, 0.3, 0.6, 1.0, 0.6, 0.3, 0.0, 0.0],
                  [0.0, 0.0, 0.3, 0.6, 0.6, 0.6, 0.3, 0.0, 0.0],
                  [0.0, 0.0, 0.3, 0.3, 0.3, 0.3, 0.3, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

BOARD_SCORES_7 = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, 0.0, 0.5, 0.5, 0.5, 0.0, 0.0],
                  [0.0, 0.0, 0.5, 1.0, 0.5, 0.0, 0.0],
                  [0.0, 0.0, 0.5, 0.5, 0.5, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

PATTERN_SCORES = {
    '5': 100000000,
    'open4': 8000000,
    'half4': 400000,
    'open3': 40000,
    'half3': 20000,
    'open2': 200,
    'half2': 100
}


def board_eval(board, player, patternS, boardS, ratio) -> float:
    """
    This function returns an float representing the heuristics of the given board.
    patternS is a dictionary with (pattern, value) pairs
    boardS is a valued board matrix

    formula: player * slot + 2
    3 for self slots
    2 for empty slots
    1 for opponent slots
    """
    self_newBoard = board.copy() * player + 2
    self_pattern_core = count_pattern_score(self_newBoard, patternS)
    self_board_score = player * np.sum(np.multiply(board, boardS))
    self_score = self_pattern_core + self_board_score

    player = -1 * player
    oppo_newBoard = board.copy() * player + 2
    oppo_pattern_core = count_pattern_score(oppo_newBoard, patternS)
    oppo_board_score = player * np.sum(np.multiply(board, boardS))
    oppo_score = oppo_pattern_core + oppo_board_score
    return self_score - ratio*oppo_score


def count_pattern_score(board, patternS):
    """
    This function returns the score of counting all patterns
    """
    # print(board)
    score = 0
    for pattern in patternS:
        count = 0
        count += search_horizontal(board, pattern)
        count += search_vertical(board, pattern)
        count += search_diagonal(board, pattern)
        value = patternS[pattern]
        if count:
            # print(str(count) + '*' + str_format(value))
            score += count * value
    return score


def search_horizontal(board, pattern):
    """
    This function returns the occurence of pattern in all rows
    """
    count = 0
    for row in board:
        s = "".join(map(str, row))
        for p in get_patterns(pattern):
            count += len(re.findall(p, s, overlapped=True))

    return count


def search_vertical(board, pattern):
    """
    This function returns the occurence of pattern in all cols
    """
    count = 0
    for col in board.copy().T:
        s = "".join(map(str, col))
        for p in get_patterns(pattern):
            count += len(re.findall(p, s, overlapped=True))

    return count


def search_diagonal(board, pattern):
    """
    This function returns the occurence of pattern in all diagonals
    """
    board = board.copy()
    diags = [board[::-1, :].diagonal(i)
             for i in range(-board.shape[0]+1, board.shape[1])]
    diags.extend(board.diagonal(i)
                 for i in range(board.shape[1]-1, -board.shape[0], -1))

    count = 0
    for diag in diags:
        s = "".join(map(str, diag))
        for p in get_patterns(pattern):
            count += len(re.findall(p, s, overlapped=True))

    return count


def get_patterns(pattern):
    """
    Gets the specifc models of each pattern
    """
    if pattern == '5':
        return ['33333']
    if pattern == 'open4':
        return ['233332']
    if pattern == 'half4':
        return ['133332', '233331']
    if pattern == 'open3':
        return ['23332']
    if pattern == 'half3':
        return ['13332', '23331']
    if pattern == 'open2':
        return ['2332']
    if pattern == 'half2':
        return ['1332', '2331']
