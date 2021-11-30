"""
This module contains testing for different AIs.
"""

from minimax import AI
from board import Game


def compare_depths(s, d1, d2, times=1):
    """
    This function returns number of wins of the given two AI. 
    s: size of the board.
    d1: depth of first AI (black, 1)
    d2: depth of second AI (white, -1)

    """
    ai1 = AI(size=s, player=1, depth=d1)
    ai2 = AI(size=s, depth=d2)

    counts = [0, 0]
    for i in range(times):
        game = Game(s)
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


# counts = compare_depths(7, 1, 2)
# print(counts)
