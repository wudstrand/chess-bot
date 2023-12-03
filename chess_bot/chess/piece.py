from dataclasses import dataclass
from typing import Optional

from chess_bot.chess.board.position import Position
from chess_bot.chess.enum.color import Color
from chess_bot.chess.enum.piece_type import PieceType


@dataclass
class Piece:
    piece_type: PieceType
    color: Color
    position: Position

    @classmethod
    def from_board(cls, marker: int, rank_idx: int, file_idx: int) -> Optional['Piece']:
        if marker == 0:
            return None
        position = Position.from_rank_and_file(rank_idx=rank_idx, file_idx=file_idx)

        if position is None:
            return None

        return cls(
            piece_type=PieceType.from_marker(marker),
            color=Color.from_marker(marker),
            position=position
        )

    def __str__(self):
        piece_name = self.piece_type.value.name
        color_name = self.color.value.name
        return f"[{color_name} {piece_name}: {self.position}]"

