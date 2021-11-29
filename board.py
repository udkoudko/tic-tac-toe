from constants import Constants
import os


class Board:
    def __init__(self, n):
        self.dimension = n
        self.playground = [
            ["-"] * self.dimension for _ in range(self.dimension)]

    def print_board(self):
        def print_line():
            print("+", end="")
            for _ in range(Constants.N):
                print("---", end="+")
            print()

        for row in range(self.dimension):
            print_line()
            print("| ", end="")
            for col in range(self.dimension):
                print(self.playground[row][col], end=" | ")
            print()

        print_line()
