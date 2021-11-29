from player import Player
from board import Board
from game import Game
from constants import Constants
from playerai import PlayerAI


def main():
    game_board = Board(Constants.N)
    player_1 = Player(Constants.PLAYER_1_SYMBOL)
    player_2 = PlayerAI(Constants.PLAYER_2_SYMBOL)
    start = input("Do you want to start ? [y/n] ")

    if start.lower() == "y":
        game = Game(game_board, player_1, player_2)
    else:
        game = Game(game_board, player_2, player_1)

    game.play()


if __name__ == "__main__":
    main()
