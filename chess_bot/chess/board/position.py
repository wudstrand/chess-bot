from dataclasses import dataclass
from typing import Optional

from chess_bot.chess.constant import Constants


@dataclass
class Rank:
    idx: int

    def __str__(self) -> str:
        value = self.idx + 1
        return str(value)

    def is_valid(self):
        return 0 <= self.idx < Constants.number_of_ranks.value


@dataclass
class File:
    idx: int

    def __str__(self) -> str:
        ordinal_value = ord("a") + self.idx
        return chr(ordinal_value)

    def is_valid(self) -> bool:
        return 0 <= self.idx < Constants.number_of_files.value


@dataclass(init=False)
class Position:
    def __init__(self, file_idx: int, rank_idx: int):
        self.file = File(idx=file_idx)
        self.rank = Rank(idx=rank_idx)

    def __str__(self) -> str:
        if not self.is_valid_position():
            return ""
        return f"{self.file}{self.rank}"

    @staticmethod
    def from_rank_and_file(rank_idx: int, file_idx: int) -> Optional['Position']:
        position = Position(
            file_idx=file_idx,
            rank_idx=rank_idx
        )
        return position if position.is_valid_position() else None

    def move(
            self,
            file_delta: int,
            rank_delta: int
    ) -> "Position":
        return Position(
            file_idx=self.file.idx + file_delta,
            rank_idx=self.rank.idx + rank_delta
        )

    def validate_position(self):
        msg = f"Invalid position: must be contained in {Constants.number_of_files.value}x{Constants.number_of_ranks.value} grid."
        if not self.is_valid_position():
            raise ValueError(msg)

    def is_valid_position(self) -> bool:
        return self.file.is_valid() and self.rank.is_valid()


