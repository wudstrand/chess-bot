import math
from dataclasses import dataclass
from enum import Enum


@dataclass
class PieceInformation:
    name: str
    marker: int
    value: float


class PieceType(Enum):
    PAWN = PieceInformation(name="pawn", marker=1, value=1.0)
    KNIGHT = PieceInformation(name="knight", marker=2, value=3.0)
    BISHOP = PieceInformation(name="bishop", marker=3, value=3.0)
    ROOK = PieceInformation(name="rook", marker=4, value=5.0)
    QUEEN = PieceInformation(name="queen", marker=5, value=8.0)
    KING = PieceInformation(name="king", marker=6, value=math.inf)

    # TODO: Can we make this more efficient?
    @staticmethod
    def from_marker(marker: int) -> 'PieceType':
        processed_marker = abs(marker)
        for piece_type in PieceType:
            if piece_type.value.marker == processed_marker:
                return piece_type
        raise ValueError(f"Invalid marker value: {marker}")

