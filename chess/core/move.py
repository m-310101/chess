from dataclasses import dataclass

CHAR_ORD_OFFSET: int = 97  # character ordinal representation offset


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


class Move:
    """
    Represents a move on the chessboard
    """

    def __init__(self) -> None:
        pass
