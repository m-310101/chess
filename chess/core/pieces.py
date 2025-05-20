from dataclasses import dataclass
from enum import Enum

CHAR_ORD_OFFSET: int = 97  # character ordinal representation offset


class PieceColour(Enum):
    """
    Enumerates the possible colours for chess pieces.

    This enum related to the possible piece colours in chess: white and black.
    """

    WHITE = 0
    BLACK = 1


@dataclass
class Position:
    """
    Represents a position on the chessboard using file and rank.

    This class encapsulates the file (column) and rank (row) of a chessboard square.
    """

    file: str  # a-h
    rank: int  # 1-8

    def is_valid(self, board_width: int = 8, board_height: int = 8):
        x, y = self.get_x_y(board_height)
        return (0 <= x < board_width) and (0 <= y < board_height)

    def to_str(self) -> str:
        return f"{self.file}{self.rank}"

    def get_x_y(self, board_height: int = 8) -> tuple[int, int]:
        return (ord(self.file) - CHAR_ORD_OFFSET), (board_height - self.rank)


class ChessPiece:
    """
    Represents a generic chess piece with a specific colour.

    This class serves as a base for all chess pieces, storing their colour.
    """

    def __init__(self, colour: PieceColour) -> None:
        self.colour = colour

    def get_piece_colour(self) -> PieceColour:
        return self.colour
