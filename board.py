"""
This module contains the static Gomoku game board.
In this game, "O" for white, "X" for black, "_" for empty.
"""

import numpy as np
from tabulate import tabulate


class Board:
    def __init__(self) -> None:
        self.board = np.zeros((15, 15)).astype(int)

    def place(self, x: int, y: int, player: int):
        """
        Player places a stone on (x,y)
        """
        if self.board[x][y] != 0:
            return False
        self.board[x][y] = player
        return True

    def print(self):
        """
        Prints the current board on the terminal.
        """
        def f(t):
            if t == 1:
                return '\033[96m'+"X"+'\033[0m'
            elif t == -1:
                return '\033[93m'+"O"+'\033[0m'
            else:
                return "_"

        f_vec = np.vectorize(f)
        indexR = np.array([["01", "02", "03", "04", "05", "06",
                            "07", "08", "09", "10", "11", "12", "13", "14", "15"]])
        indexC = np.array([["  ", "01", "02", "03", "04", "05", "06",
                            "07", "08", "09", "10", "11", "12", "13", "14", "15"]])
        copied = np.copy(self.board)
        copied = f_vec(copied)
        concat = np.concatenate((indexR, copied), axis=0)
        concated = np.concatenate((indexC.T, concat), axis=1)
        print("\n")

        print(tabulate(concated))
        print("\n")

    def check(self, x, y, player):
        """
        Return True if current player wins.
        """
        consecs = []

        for d in [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1]]:
            i = d[0]
            j = d[1]
            if not i and not j:
                continue
            cx, cy = x, y
            count = 0
            while 0 <= cx < 15 and 0 <= cy < 15 and self.board[cx][cy] == player:
                count += 1
                cx += i
                cy += j
            consecs.append(count)
        # print(consecs)
        for i in range(0, 8, 2):
            if consecs[i]+consecs[i+1]-1 >= 5:
                return True

        return False


# class Board:
#     def __init__(self) -> None:
#         self.board = [[" _" for _ in range(16)] for _ in range(16)]
#         self.board[0] = ["  ", "01", "02", "03", "04", "05", "06",
#                          "07", "08", "09", "10", "11", "12", "13", "14", "15"]
#         for i in range(1, 16):
#             if i < 10:
#                 self.board[i][0] = "0"+str(i)
#             else:
#                 self.board[i][0] = str(i)

#     def place(self, x: int, y: int, player: str):
#         """
#         Player places a stone on (x,y)
#         """
#         if self.board[x][y] != " _":
#             return False
#         self.board[x][y] = player
#         return True

#     def print(self):
#         """
#         Prints the current board on the terminal.
#         """
#         print("\n")
#         print('\n'.join([' '.join([str(cell) for cell in row])
#                          for row in self.board]))
#         print("\n")

#     def check(self, x, y, player):
#         """
#         Return True if current player wins.
#         """
#         consecs = []

#         for d in [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1]]:
#             i = d[0]
#             j = d[1]
#             if not i and not j:
#                 continue
#             cx, cy = x, y
#             count = 0
#             while 1 <= cx <= 15 and 1 <= cy <= 15 and self.board[cx][cy] == player:
#                 count += 1
#                 cx += i
#                 cy += j
#             consecs.append(count)
#         # print(consecs)
#         for i in range(0, 8, 2):
#             if consecs[i]+consecs[i+1]-1 >= 5:
#                 return True

#         return False
