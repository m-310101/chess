from enum import Enum

from board import ChessBoard


class PieceColour(Enum):
    """
    Enumerates the possible colours for chess pieces.

    This enum related to the possible piece colours in chess: white and black.
    """

    WHITE = 0
    BLACK = 1


class ChessPiece:
    """
    Represents a generic chess piece with a specific colour.

    This class serves as a base for all chess pieces, storing their colour.
    """

    def __init__(self, colour: PieceColour) -> None:
        self.colour = colour

    def get_piece_colour(self) -> PieceColour:
        return self.colour

    def get_valid_moves(self, board: "ChessBoard") -> "list[Move]":
        raise NotImplementedError
