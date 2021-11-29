from player import Player
import random as rand
from constants import Constants


class PlayerAI(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def make_move(self, board):
        while True:
            col = rand.randint(0, Constants.N - 1)
            row = rand.randint(0, Constants.N - 1)

            if board.playground[row][col] == "-":
                return (row, col)
            else:
                print("Select valid coordinates")
