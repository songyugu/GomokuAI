"""
This module contains testing for different AIs.
"""

from minimax import AI
from board import Board

ai1 = AI(depth=1)
ai2 = AI(depth=2)


def train_heuristics(a1, a2, times=10):
    """
    This function returns number of wins of the given two AI. a1 is player 1 (Black) and a2 is -1 (White).
    """
    counts = [0, 0]
    for i in range(times):
        game = Board()
        player = 1
        winning = False

        while not winning:
            # print(player)
            if player == 1:  # black's turn
                x, y = ai1.minimax(game.board, player)
                game.place(x, y, player)
                if game.check(x, y, player):
                    winning = True
                    counts[0] += 1
                else:
                    player = -player

            else:
                x, y = ai2.minimax(game.board, player)
                game.place(x, y, player)
                if game.check(x, y, player):
                    winning = True
                    counts[1] += 1
                else:
                    player = -player
    # game.print()
    return counts


counts = train_heuristics(ai1, ai2)
print(counts)
