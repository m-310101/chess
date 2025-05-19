from dataclasses import dataclass
from enum import Enum


class PieceColour(Enum):
    WHITE = 0
    BLACK = 1


@dataclass
class Position:
    file: str  # a-h
    rank: int  # 1-8
