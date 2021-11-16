"""
This is the main entry where the game is played.
"""
from board import Game
from minimax import AI


def human_vs_ai(size):
    """
    This function is where human player plays with AI in the terminal. 
    The human player plays first with Black (1) and AI with White (-1).
    The board size can be other 7, 9, or 15.
    """
    game = Game(size)
    player = 1
    winning = False
    ai = AI(size)

    CRED = '\033[92m'
    CEND = '\033[0m'
    print(CRED+"Welcome to our Gomoku game! \nEnter \'quit\' to quit the game."+CEND)
    game.print()

    while not winning:
        if player == 1:  # black's turn
            choice = input(
                "Please enter \"row col\" where you want to place a BLACK stone.\n")
            if choice == "quit":
                return
            try:
                inputs = choice.split(" ")

                if game.place(int(inputs[0]), int(inputs[1]), player):
                    game.print()
                    if game.check(int(inputs[0]), int(inputs[1]), player):
                        CRED = '\033[96m'
                        CEND = '\033[0m'
                        print(CRED + "Black wins." + CEND)
                        winning = True
                    else:
                        player = -1
                else:
                    CRED = '\033[91m'
                    CEND = '\033[0m'
                    print(CRED + "Slot already taken." + CEND)
            except:
                CRED = '\033[91m'
                CEND = '\033[0m'
                print(
                    CRED + "Please input a valid row, col pair separated by an empty space." + CEND)

        else:
            x, y = ai.minimax(game.board, player)
            if game.place(x, y, player):
                game.print()
                if game.check(x, y, player):
                    CRED = '\033[93m'
                    CEND = '\033[0m'
                    print(CRED + "White wins." + CEND)
                    winning = True
                else:
                    player = 1


if __name__ == "__main__":

    human_vs_ai(7)
