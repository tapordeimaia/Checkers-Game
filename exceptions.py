class InvalidMoveException(Exception):
    def __init__(self, message = "Invalid move"):
        self._message = message

    def __str__(self):
        return self._message

class OutOfBoardException(InvalidMoveException):
    def __init__(self):
        super().__init__("Move is out of the board.")

class NotDarkSquareException(InvalidMoveException):
    def __init__(self):
        super().__init__("Move is not a dark square.")

class InitialSymbolValidException(InvalidMoveException):
    def __init__(self):
        super().__init__("The initial space should have the respective symbol.")

class DestinationNotEmptyException(InvalidMoveException):
    def __init__(self):
        super().__init__("The destination is not empty")

class InvalidJumpException(InvalidMoveException):
    def __init__(self):
        super().__init__("You can only jump over an opponent's piece")

class InvalidDirectionException(InvalidMoveException):
    def __init__(self):
        super().__init__("Pieces can only move forward")

class InvalidInputException(InvalidMoveException):
    def __init__(self):
        super().__init__("Invalid input, must be from 0 to 7")

class GameOver(Exception):
    pass

