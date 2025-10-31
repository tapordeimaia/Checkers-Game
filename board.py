from texttable import Texttable

from exceptions import OutOfBoardException, NotDarkSquareException, InitialSymbolValidException, \
    DestinationNotEmptyException, InvalidJumpException, InvalidDirectionException, InvalidMoveException, \
    InvalidInputException

CHECK_IF_EVEN = 2
PLAYER_RANGE = 3
COMPUTER_RANGE = 4
VALID_ROW_DIFFERENCE = 2
OTHER_VALID_ROW_DIFFERENCE = 1
ANOTHER_VALID_ROW_DIFFERENCE = -1
FIRST_ROW = 0
SIZE = 8
NOT_VALID = False
VALID = True

class CheckersBoard:
    def __init__(self, size=SIZE, symbol=' '):
        self._size = size
        self._symbol = symbol
        self._boards = [[' ' for _ in range(self._size)] for _ in range(self._size)]

    @property
    def size(self):
        return self._size

    @property
    def board(self):
        return self._boards

    def __str__(self):
        table = Texttable()
        header = [' '] + [str(i) for i in range(self._size)]
        table.header(header)

        for i in range(self._size):
            row = [str(i)] + self._boards[i]
            table.add_row(row)

        return table.draw()

    def place_checkers(self):
        for row in range(self._size):
            for column in range(self._size):
                if row % CHECK_IF_EVEN == column % CHECK_IF_EVEN:
                    if row < PLAYER_RANGE:
                        self._boards[row][column] = 'X'
                    elif row > COMPUTER_RANGE:
                        self._boards[row][column] = 'O'
                    else:
                        self._boards[row][column] = ' ' # Dark square
                else:
                    self._boards[row][column] = '.' # Light square
        return self._boards

    def is_valid_move(self, initial_row, initial_column, final_row, final_column, symbol):
        if self._boards[initial_row][initial_column] == " ":
            raise InvalidMoveException

        # Ensure the input is valid
        if initial_row not in range(0, self._size) and initial_column not in range(0, self._size) and final_row not in range(0, self._size) and final_column not in range(0, self._size):
            raise InvalidInputException()

        # Ensure the move is within the board
        if not (0 <= initial_row < self._size and 0 <= initial_column < self._size and
                0 <= final_row < self._size and 0 <= final_column < self._size):
            raise OutOfBoardException()

        # Ensure the piece is moving on a dark square
        if final_row % CHECK_IF_EVEN != final_column % CHECK_IF_EVEN:
            raise NotDarkSquareException()

        # Ensure the initial position has the correct piece
        if self._boards[initial_row][initial_column] != symbol:
            raise InitialSymbolValidException()

        # Ensure the destination is empty
        if self._boards[final_row][final_column] != ' ':
            raise DestinationNotEmptyException()

        # Calculate move direction and distance
        row_difference = final_row - initial_row
        column_difference = final_column - initial_column



        # If not a simple move or valid jump, return False
        if abs(row_difference) != OTHER_VALID_ROW_DIFFERENCE or abs(column_difference) != OTHER_VALID_ROW_DIFFERENCE:
            if 'K' in symbol:
                if abs(row_difference) == abs(column_difference):
                    step_row = int(row_difference / abs(row_difference))
                    step_column = int(column_difference / abs(column_difference))
                    current_row, current_column = initial_row, initial_column

                    while current_row != final_row - step_row and current_column != final_column - step_column:
                        current_row += step_row
                        current_column += step_column

                        if self._boards[final_row][final_column] != ' ':
                            return NOT_VALID
                    return VALID

                raise InvalidMoveException()

        return VALID




    def move_checkers(self, initial_row, initial_column, final_row, final_column):
        symbol = self._boards[initial_row][initial_column]
        if not self.is_valid_move(initial_row, initial_column, final_row, final_column, symbol):
            raise InvalidMoveException

        #if abs(initial_row - final_row) == VALID_ROW_DIFFERENCE and abs(initial_column - final_column) == VALID_ROW_DIFFERENCE:
        row_step = 1 if final_row > initial_row else -1
        col_step = 1 if final_column > initial_column else -1
        path = []
        current_row, current_column = initial_row + row_step, initial_column + col_step
        while (current_row, current_column) != (final_row, final_column):
            path.append((current_row, current_column))
            current_row += row_step
            current_column += col_step
        for current_row, current_column in path:
            self._boards[current_row][current_column] = " "

        self._boards[final_row][final_column] = self._boards[initial_row][initial_column]
        self._boards[initial_row][initial_column] = ' '
        self.promote_kings()




    def promote_kings(self):
        for column in range(self._size):
            if self._boards[FIRST_ROW][column] == 'O':
                self._boards[FIRST_ROW][column] = 'KO'
            if self._boards[self._size - 1][column] == 'X':
                self._boards[self._size - 1][column] = 'KX'

    def check_if_game_over(self):
        over = True
        for row in range(self._size):
            for column in range(self._size):
                if self._boards[row][column] == 'O' or self._boards[row][column] == 'KO':
                    over = False
        return over














