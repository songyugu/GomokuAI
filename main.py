"""
This is the main entry where the game is played.
"""
from board import Board
import minimax


if __name__ == "__main__":
    game = Board()
    game.print()
    turn = True
    winning = False
    while not winning:
        if turn:  # black's turn
            choice = input(
                "Please enter \"row col\" where you want to place a BLACK stone.\n")
            inputs = choice.split(" ")
            if game.place(int(inputs[0]), int(inputs[1]), '\033[96m'+" X"+'\033[0m'):
                game.print()
                if game.check(int(inputs[0]), int(inputs[1]), '\033[96m'+" X"+'\033[0m'):
                    CRED = '\033[96m'
                    CEND = '\033[0m'
                    print(CRED + "Black wins." + CEND)
                    winning = True
                else:
                    turn = not turn
            else:
                CRED = '\033[91m'
                CEND = '\033[0m'
                print(CRED + "Slot already taken." + CEND)

        else:
            x, y = minimax.next_move(game.board, "O")
            if game.place(x, y, '\033[93m'+" O"+'\033[0m'):
                game.print()
                if game.check(x, y, '\033[93m'+" O"+'\033[0m'):
                    CRED = '\033[93m'
                    CEND = '\033[0m'
                    print(CRED + "White wins." + CEND)
                    winning = True
                else:
                    turn = not turn

            # choice = input(
            #     "Please enter \"row col\" where you want to place a WHITE stone.\n")
            # inputs = choice.split(" ")
            # if game.place(int(inputs[0]), int(inputs[1]), '\033[93m'+" O"+'\033[0m'):
            #     game.print()
            #     if game.check("O"):
            #         print("White wins.")
            #         winning = True
            #     else:
            #         turn = not turn
            # else:
            #     CRED = '\033[91m'
            #     CEND = '\033[0m'
            #     print(CRED + "Slot already taken." + CEND)
