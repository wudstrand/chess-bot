from dataclasses import dataclass
from typing import Tuple

from chess_bot.chess.constant import Constants


@dataclass
class Position:
    x: int
    y: int

    def __post_init__(self) -> None:
        self.validate_position()

    def __str__(self) -> str:
        file, rank = self.location()
        return f"{file}{rank}"

    @staticmethod
    def from_rank_and_file(rank_idx: int, file_idx: int) -> 'Position':
        return Position(
            x=file_idx,
            y=rank_idx
        )

    def move(self, x: int, y: int) -> "Position":
        return Position(x=self.x + x, y=self.y + y)

    def validate_position(self):
        msg = f"Invalid position: must be contained in {Constants.number_of_files}x{Constants.number_of_ranks} grid."
        if not self.is_valid_position():
            raise ValueError(msg)

    def is_valid_position(self) -> bool:
        valid_file = (0 <= self.x < Constants.number_of_files)
        valid_rank = (0 <= self.y < Constants.number_of_ranks)
        return valid_file and valid_rank

    def location(self) -> Tuple[str, int]:
        return self.file, self.rank

    @property
    def file(self) -> str:
        ordinal_value = ord("a") + self.x
        return chr(ordinal_value)

    @property
    def rank(self) -> int:
        return self.y + 1


