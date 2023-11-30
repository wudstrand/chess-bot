from dataclasses import dataclass
from typing import Tuple

from src.chess.constant import Constants


@dataclass
class Position:
    x: int
    y: int

    def __post_init__(self) -> None:
        self.validate_position()

    def __str__(self) -> str:
        file, rank = self.location()
        return f"{file}{rank}"

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
        rank = self.rank()
        file = self.file()
        return file, rank

    def file(self) -> str:
        ordinal_value = ord("a") + self.x
        return chr(ordinal_value)

    def rank(self) -> int:
        return self.y + 1


