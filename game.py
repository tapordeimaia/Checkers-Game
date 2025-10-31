import random

TOP_LEFT = (-1, -1)
TOP_RIGHT = (-1, 1)
BOTTOM_LEFT = (1, -1)
BOTTOM_RIGHT = (1, 1)
JUMP_TOP_LEFT = (-2, -2)
JUMP_TOP_RIGHT = (-2, 2)
JUMP_BOTTOM_LEFT = (2, -2)
JUMP_BOTTOM_RIGHT = (2, 2)
FINAL_ROW = 0
FINAL_COLUMN = 1
JUMP_MOVE_INDEX = 2
SIZE = 8
ALL_DIAGONALS = [TOP_LEFT, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_RIGHT]
JUMP_DIAGONALS = [JUMP_TOP_LEFT, JUMP_TOP_RIGHT, JUMP_BOTTOM_LEFT, JUMP_BOTTOM_RIGHT]
SIMPLE_MOVE = False
JUMP_MOVE = True

class ComputerGame:
    def __init__(self, board):
        self._board = board

    def get_valid_move(self, row, column, is_king = False):
        valid_moves = []
        symbol = self._board.board[row][column]
        opponent_symbol = 'X' if 'O' in symbol else 'O'
        is_king = 'K' in symbol
        directions = ALL_DIAGONALS if is_king else [TOP_LEFT, TOP_RIGHT]
        for direction_row, direction_column in directions:
            final_row = row + direction_row
            final_column = column + direction_column
            if 0 <= final_row < self._board.size and 0 <= final_column < self._board.size:
                if self._board.board[final_row][final_column] == ' ':
                    valid_moves.append((final_row, final_column, SIMPLE_MOVE))

        jump_directions = JUMP_DIAGONALS if is_king else [JUMP_TOP_LEFT, JUMP_TOP_RIGHT]
        for direction_row, direction_column in jump_directions:
            final_row = row + direction_row
            final_column = column + direction_column
            middle_row = (row + final_row) // 2
            middle_column = (column + final_column) // 2
            if (0 <= final_row < self._board.size and 0 <= final_column < self._board.size and
                    self._board.board[middle_row][middle_column] in [opponent_symbol, f'K{opponent_symbol}'] and
                    self._board.board[final_row][final_column] == ' '):
                valid_moves.append((final_row, final_column, JUMP_MOVE))


        return valid_moves


    def move_checker(self):
        symbol = "O"
        all_pieces = []
        for row in range(self._board.size):
            for column in range(self._board.size):
                if self._board.board[row][column] in [symbol, f'K{symbol}']:
                    all_pieces.append((row, column))

        all_valid_moves = []
        for row, column in all_pieces:
            is_king = 'K' in self._board.board[row][column]
            valid_moves = self.get_valid_move(row, column, is_king)
            for move in valid_moves:
                all_valid_moves.append((row, column, move[FINAL_ROW], move[FINAL_COLUMN], move[JUMP_MOVE_INDEX]))

        if not all_valid_moves:
            return

        jump_moves = [move for move in all_valid_moves if move[4]]
        if jump_moves:
            selected_move = random.choice(jump_moves)
        else:
            selected_move = random.choice(all_valid_moves)

        initial_row, initial_column, final_row, final_column, is_jump = selected_move
        self._board.move_checkers(initial_row, initial_column, final_row, final_column)

        if is_jump:
            self.perform_multiple_jumps(final_row, final_column)

    def perform_multiple_jumps(self, row, column):
        valid_jump_moves = self.get_valid_move(row, column, is_king=('K' in self._board.board[row][column]))
        jump_moves = [move for move in valid_jump_moves if move[JUMP_MOVE_INDEX] == JUMP_MOVE]

        if jump_moves:
            selected_move = random.choice(jump_moves)
            final_row, final_column, _ = selected_move
            self._board.move_checkers(row, column, final_row, final_column)

            self.perform_multiple_jumps(final_row, final_column)

    def check_if_game_over(self):
        over = True
        for row in range(SIZE):
            for column in range(SIZE):
                if self._board.board[row][column] == 'X' or self._board.board[row][column] == 'KX':
                    over = False
        return over






