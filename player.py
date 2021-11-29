import random as rand
from constants import Constants


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

        self.rows_container = [0 for _ in range(Constants.N)]
        self.columns_container = [
            0 for _ in range(Constants.N)]
        self.diagonal_container = [0 for _ in range(Constants.N)]
        self.opposite_diagonal_container = [0 for _ in range(Constants.N)]

    def check_win(self):
        if (Constants.N in self.rows_container or
            Constants.N in self.columns_container or
            self.check_diagonal() or
                self.check_opposite_diagonal()):
            return True

        return False

    def check_diagonal(self):
        result = all(el == 1
                     for el in self.diagonal_container)

        return result

    def check_opposite_diagonal(self):
        result = all(el == 1
                     for el in self.opposite_diagonal_container)

        return result

    def make_move(self, board):
        while True:
            try:
                col = int(input("Select column: ")) - 1
                row = int(input("Select row: ")) - 1

                if board.playground[row][col] == "-":
                    return (row, col)
                else:
                    print("Select valid coordinates")
                    continue

            except ValueError:
                print("Input should be integer value")
                continue
            except IndexError:
                print("Input should be in range [0 - n-1]")
                continue
