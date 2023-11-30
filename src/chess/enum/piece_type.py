import math
from dataclasses import dataclass
from enum import Enum


@dataclass
class PieceInformation:
    name: str
    value: float


class PieceType(Enum):
    PAWN = PieceInformation(name="pawn", value=1.0)
    KNIGHT = PieceInformation(name="knight", value=3.0)
    BISHOP = PieceInformation(name="bishop", value=3.0)
    ROOK = PieceInformation(name="rook", value=5.0)
    QUEEN = PieceInformation(name="queen", value=8.0)
    KING = PieceInformation(name="king", value=math.inf)
