class ChessBoard:
    def __init__(self, width: int = 8, height: int = 8) -> None:
        self.width: int = width
        self.height: int = height

        self._makeboard()

    def _makeboard(self) -> None:
        self.squares: list[list[ChessPiece | None]] = [
            [None for _ in range(self.width)] for _ in range(self.height)
        ]

    def getBoard(self) -> list[list[ChessPiece | None]]:
        return self.squares

    def getPieceAt(self, position: Position) -> ChessPiece | None:
        pass

    def toFEN(self) -> str:
        # TODO: create logic to return FEN representation of board https://www.chess.com/terms/fen-chess (add FEN letters to piece class)
        pass
