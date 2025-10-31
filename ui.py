from board import CheckersBoard
from exceptions import GameOver, InvalidMoveException
from game import ComputerGame
from colorama import Fore, Style


class UI:
    def __init__(self):
        self._board = CheckersBoard()
        self._computer_game = ComputerGame(self._board)

    def create_board(self):
        self._board.place_checkers()

    def print_board(self):
        print(Fore.RED)
        print(self._board)
        print(Style.RESET_ALL)

    def start_game(self):
        self.create_board()
        self.print_board()
        human_turn = True
        while True:
            if human_turn:
                try:
                    initial_row = int(input("Enter intial row: "))
                    initial_column = int(input("Enter intial column: "))
                    final_row = int(input("Enter the final row: "))
                    final_column = int(input("Enter the final column: "))
                    self._board.move_checkers(initial_row, initial_column, final_row, final_column)
                    self.print_board()
                    if self._board.check_if_game_over():
                        print("You won!!!")
                        break
                    human_turn = False
                except InvalidMoveException as error:
                    print(error)
            else:
                try:
                    self._computer_game.move_checker()
                    self.print_board()
                    if self._computer_game.check_if_game_over():
                        print("You lost.")
                        break
                    human_turn = True
                except InvalidMoveException as error:
                    print(error)


