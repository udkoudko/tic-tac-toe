import random as rand
import os

from board import Board
from constants import Constants


class Game:
    def __init__(self, board, player_1, player_2) -> None:
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.is_game_running = True
        self.curr_player = self.player_1

    def play(self):
        while self.is_game_running:
            os.system("cls")
            print(f"Player {self.curr_player.symbol} is on the move")
            self.board.print_board()
            self.make_move()

    def check_tie(self):
        count = 0
        for row in self.board.playground:
            if "-" not in row:
                count += 1

        if count == self.board.dimension:
            return True

        return False

    def make_move(self):
        def end_move():
            self.is_game_running = False
            os.system("cls")
            print(self.board.print_board())

        row, col = self.curr_player.make_move(self.board)
        self.board.playground[row][col] = self.curr_player.symbol

        self.curr_player.rows_container[row] += 1
        self.curr_player.columns_container[col] += 1

        if row == col:
            self.curr_player.diagonal_container[row] += 1

        if row + col + 1 == Constants.N:
            self.curr_player.opposite_diagonal_container[row] += 1

        if self.check_tie():
            end_move()
            print("TIE !")
        elif self.curr_player.check_win():
            end_move()
            print(f"Player {self.curr_player.symbol} won !!!!")
        else:
            self.curr_player = self.player_2 if self.curr_player == self.player_1 else self.player_1
