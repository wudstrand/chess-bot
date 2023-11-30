from abc import ABC, abstractmethod
from typing import Set

from src.chess.board.position import Position
from src.chess.enum.piece_type import PieceType


class AbstractPiece(ABC):
    def __init__(
        self,
        piece_type: PieceType,
        position: Position
    ):
        self.piece_type = piece_type
        self.position = position
        self.position_history = [position]

    @abstractmethod
    def calculate_legal_moves(self) -> Set[Position]:
        pass

    @abstractmethod
    def foobar(self):
        pass
